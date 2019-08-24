x = True
y = False
a = ('cat', 'dog', 'bird', 'fish')
b = 'cat'

print(f'x={x}, y={y}, a={a}, b={b}')
if x and y:
    print('x and y = True')
else:
    print('x and y = False')

if x or y:
    print('x or y = True')
else:
    print('x or y = False')

if not x:
    print('not x = True')
else:
    print('not x = False')

if b not in a:
    print('b not in a = True')
else:
    print('b not in a = False')

if b is a[0]:
    print('b is a[0] = True')
else:
    print('b is a[0] = False')

if b is not a[1]:
    print('b is not a[0] = True')
else:
    print('b is not a[0] = False')