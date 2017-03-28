import numpy as np
import pylab as plb
import matplotlib.pyplot as plt

def dev_from_mean(x):
    xmean = plb.mean(x)
    return [xi - xmean for xi in x]

#Covariance (can be positive/negative)
# small covariance means there is not much relationship between the two.
# large covariance means we need to figure out how large it has to be
# before we can say they are related. Enter Correlation.
# cor == 0 ? no relationship
# corr == 1 ? direct relationship
# corr == -1 ? inverse relationship

def covariance(x,y):
    n = len(x)
    x_dev = dev_from_mean(x)
    y_dev = dev_from_mean(y)
    return plb.dot(x_dev, y_dev)/(n-1)

def correlation(x,y):
    stdx = x.std()
    stdy = y.std()
    return covariance(x,y)/stdx/stdy

# correlation is not causality

pageRenderTime = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - pageRenderTime * 2 # negative correlation
purchaseAmount = 10 + pageRenderTime * 2 # positive correlation
#purchaseAmount = np.random.normal(50.0, 10.0, 1000) /pageRenderTime # remove this division for a random plot.

fig1 = plt.figure(1)
fig1.suptitle("Render time v Purchase amt")
plt.xlabel("Render time")
plt.ylabel("Purchase amt")
plt.grid()
plt.scatter(pageRenderTime, purchaseAmount)

#print('covar = %f' % covariance(pageRenderTime, purchaseAmount)) really slow
#print('correl = %f' % correlation(pageRenderTime, purchaseAmount))
# interpret as
#       var 1   | var 2
# var 1|  1x1   | 1x2   |
# var 2|  2x1   | 2x2   |
#
print('Numpy Correlation')
print(np.corrcoef(pageRenderTime, purchaseAmount))
print('Numpy Covariance')
print(np.cov(pageRenderTime, purchaseAmount))
plt.show()

