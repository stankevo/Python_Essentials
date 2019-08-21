
x = [1,2,3,4]
print(x)
print('x is a list, it is mutable.')
x[3]=42
print(x)
for i in x:
    print('i is {}'.format(i))
print()


x = (1,2,3,4)
print(x)
print('x is a tuple, it is immutable.')
for i in x:
    print('i is {}'.format(i))
print()


x = {'one':1, 'two':2, 'three':3}
print(x)
print('x is a dictionary, it is mutable.')
x['one'] = 42
print(x)
for k, v in x.items():
    print('k is {}, v is {}'.format(k,v))
print()

x = range(3)
print(x)
print('x is a range, it is immutable.')
for i in x:
    print('i is {}'.format(i))
print()

x = range(3,7)
print(x)
print('x is a range, it is immutable.')
for i in x:
    print('i is {}'.format(i))
print()

x = range(50,100,10)
print(x)
print('x is a range, it is immutable.')
for i in x:
    print('i is {}'.format(i))
print()

x = list(range(50,100,10))
print(x)
print('x is a range converted to a list, it is mutable.')
x[2] = 100000
for i in x:
    print('i is {}'.format(i))
print()



