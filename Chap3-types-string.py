
x = 7
print('x = {}'.format(x))
print(type(x))
print()

y = 7.0
print('y = {}'.format(y))
print(type(y))
print()

z = '7.0'
print('z = {}'.format(z))
print(type(z))
print()

a = None
print('a = {}'.format(a))
print(type(a))
print()

b = True
print('b = {}'.format(b))
print(type(b))
print()

print('----------PART 2--------------')

c = 'seven'.upper()
print('c is {}'.format(c))
print()

c1 = ''' 

seven

'''.capitalize()
print('c1 is {}'.format(c1))
print()


c3 = 'seven {1:<09} {0:>09}'.format(81,91)
print('c3 = {}'.format(c3))
print()


c4 = 81
c5 = 91
c6 = f'seven {c4:<09} {c5:>09}'
print('c6 = {}'.format(c6))
print(type(c6))
print()