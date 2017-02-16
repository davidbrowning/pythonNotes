#!/usr/bin/python3


d = {'key1':10, 'key2':20}
_key_iter = iter(d)
for key in _key_iter:print(key)

print('\n\n----------------------print key, value---------\n\n')
for k,v in d.items():
    print (k,v)

print('\n\n----------------------print value------------------\n\n')
for k,v in d.items():
    print (v)


print('\n\n----------------------mid----------------------\n\n')
sum(range(101))
xr = range(101)
mid = (min(xr) + max(xr)/2.0)
print(mid)

############################################################################################################################
# The following may be super useful
#
#  Notice that you have two iterables insize the zip function
#   and I'm printing the mappings of one to the other
#
############################################################################################################################
print('\n\n----------------------zip----------------------\n\n')
for n, f in zip(range(8), range(8)):
    print (n, '->', f)

print('\n\n----------------------generator----------------\n\n')
def gen_1234():
    yield 1
    yield 2
    yield 3
    yield 4

g = gen_1234()
print(g)
#for n in range(4):
    #print(g.next())



print('\n\n----------------------Py3 method---------------\n\n')
g = gen_1234()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print('\n\n----------------------More Straightforward-----\n\n')
for x in gen_1234():
    print (x)


print('\n\n----------------------Generator Expression-----\n\n')
g = (i for i in range(11) if i % 2 == 0)
#list(g)
print(list(g))

############################################################################################################################
# Generator expressions do not construct iterables; they construct generation
# Generator expressions are used in iterations
# Once the iteration is over, it cannot be restarted.
#
#
############################################################################################################################

print('\n\n---------Functions that consume generators-----\n\n')
print(sum(n for n in range(11) if n % 2 == 0))



