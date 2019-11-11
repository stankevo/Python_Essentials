x = '47'
y = int(x)
z = float(x)
print(f'x type: {type(x)}')
print(f'x = {x}')
print(f'y type: {type(y)}')
print(f'y = {y}')
print(f'z type: {type(z)}')
print(f'z = {z}')

a = -47.0
b = abs(a)
print(f'b = {b}')

q = complex(y, 73)
print(f'q type: {type(q)}')
print(f'q = {q}')

s = 47 + 56j
print(f's type: {type(s)}')
print(f's = {s}')

r = divmod(y, 3)
print(f'r type: {type(r)}')
print(f'r = {r}')
