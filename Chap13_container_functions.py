# zip
print('zip:')
x = (1,2,3,4,5)
y = ('cat', 'dog', 'rabbit', 'velociraptor')
z = zip(x,y)
for i, j in z:
    print(f'{i} - {j}')

# enumerate
print('\nenumerate:')
q = ('cat', 'dog', 'rabbit', 'velociraptor')
for i,j in enumerate(q):
    print(f'{i} - {j}')

# len
print('\nlen:')
w = ('cat', 'dog', 'rabbit', 'velociraptor')
print(w)
print(f'length of w is {len(w)}')

# list
print('\nlist:')
e = (1,2,3,4,5)
r = list(e)
print(e)
print(r)

# reverced
print('\nreverced:')
t = reversed(r)
print(t)
for i in t:
    print(i, end = ' ')
print()
g = list(reversed(r))
print(f'a list from the reversed iterator: {g}')

# sum, max, min
print('\nsum, max, min:')
o = (1,2,3,4,5)
print(o)
print(f'sum: {sum(o)}')
print(f'sum(o, 10): {sum(o, 10)}')
print(f'min: {min(o)}')
print(f'max: {max(o)}')

# any, all
print('\nany, all:')
p = (0,0,0,0,0)
s = (0,1,0,0,0)
print(f'p: {p}')
print(f's: {s}')
print(f'any(p): {any(p)}')
print(f'any(s): {any(s)}')
d = (1,2,3,4,5)
f = (1,0,3,4,5)
print(f'd: {d}')
print(f'f: {f}')
print(f'all(d): {all(d)}')
print(f'all(f): {all(f)}')