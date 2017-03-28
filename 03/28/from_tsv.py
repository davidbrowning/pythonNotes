import scipy as sp
import sys
import matplotlib.pyplot as plt

data = sp.genfromtxt(sys.argv[1], delimiter='\t')

print(data[:10])
print data.shape

x = data[:,0] # hours
y = data[:,1] # server hits

if sp.sum(sp.isnan(y)) > 0:
    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

def error(f, x, y):
    return sp.sum((f(x) - y)**2)

# if you give a numpy arra a boolean, it will give you the elements which meet that boolean. ^^ see above

pcoeffs, err, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

print('Model coeffs: %s' % pcoeffs)
f1 = sp.poly1d(sp.polyfit(x,y,1))
f2 = sp.poly1d(sp.polyfit(x,y,2))
f3 = sp.poly1d(sp.polyfit(x,y,3))
f10 = sp.poly1d(sp.polyfit(x,y,10))

print('Model error: %s' % err)
print('Linear error: %s' % error(f1,x,y))
print('Quadratic error: %s' % error(f2,x,y))
print('Cubic error: %s' % error(f3,x,y))
#print(sp.linspace(0,1,2))
# linspace presents the divisions


plt.scatter(x,y)
plt.title('Web traffic over the last month')
plt.xlabel('time')
plt.ylabel('Hits/hour')
plt.autoscale(tight = True)
plt.grid()
xvals = sp.linspace(0,x[-1], 1000)
plt.plot(xvals, f1(xvals), linewidth=4)
#plt.legend(['d=%d' % f2.order], loc='upper left')
#plt.legend(['d=%d' % f3.order], loc='upper left')
#plt.show()
plt.plot(xvals, f2(xvals), linewidth=4)
#plt.show()
plt.plot(xvals, f3(xvals), linewidth=4)
plt.plot(xvals, f10(xvals), linewidth=4)
plt.legend(['d=%d' % f1.order,'d=%d' % f2.order,'d=%d' % f3.order, 'd=%d' %f10.order], loc='upper left')
plt.show()
