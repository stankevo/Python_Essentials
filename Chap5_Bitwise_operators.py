x = 0x0a
y = 0x05
z = x & y
print(f'(hex) \nx = {x:02x} \ny = {y:02x} \n------- \nz = {z:02x}')
print(f'\n(bin) & \nx = {x:08b} \ny = {y:08b} \n------------ \nz = {z:08b}')

z = x | y
print(f'\n(bin) | \nx = {x:08b} \ny = {y:08b} \n------------ \nz = {z:08b}')

z = x ^ y
print(f'\n(bin) ˆ \nx = {x:08b} \ny = {y:08b} \n------------ \nz = {z:08b}')

y = 0x2
z = x << y
print(f'\n(bin) << \nx = {x:08b} \ny = {y:08b} \n------------ \nz = {z:08b}')

y = 0x2
z = x >> y
print(f'\n(bin) >> \nx = {x:08b} \ny = {y:08b} \n------------ \nz = {z:08b}')