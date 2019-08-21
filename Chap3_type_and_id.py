x = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(id(x))
print('Type of second element:')
print(type(x[1]))
print('Id of second element:')
print(id(x[1]))
print()

y = [1, 'two', 3.0, [4, 'four'], 5]
print('y is {}'.format(y))
print(type(y))
print(id(y))
print('Type of third element:')
print(type(y[2]))
print('Id of second element:')
print(id(y[1]))
print()

print('Are x and y the same element?')
if x is y:
    print('yep')
else:
    print('nope')
print()

print('Are x[1] and y[1] the same element?')
if x[1] is y[1]:
    print('yep')
else:
    print('nope')
print()

print('Check type of x via type() function. It will not work.')
if type(x) == 'tuple':
    print('tuple')
elif type(x) == 'list':
    print('list')
else:
    print('not a tuple, not a list')
print()


print('Check type of x via isinstance() function. It will work.')
if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print('list')
else:
    print('not a tuple, not a list')
print()

print('Check type of y via isinstance() function. It will work.')
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('not a tuple, not a list')
print()





