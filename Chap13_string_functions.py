class bunny:
    def __init__(self, n):
        self._n = n

    def __str__(self):
        return(f'str: number of bunnies is {self._n} {chr(128406)}')

    def __repr__(self):
        return(f'repr: number of bunnies is {self._n} {chr(128406)}')

class bunny2:
    def __init__(self, n):
        self._n = n

x = bunny(47)
print(x)
print(str(x))
print(repr(x))
print(ascii(x))


print('------ class without __str__ and __repr__: ------')
y = bunny2(47)
print(y)
print(str(y))
print(repr(y))
print(ascii(y))

print('----------')
print('🖖')
print(ascii('🖖'))
print(repr('🖖'))
print(ord('🖖'))
print(chr(128406))


