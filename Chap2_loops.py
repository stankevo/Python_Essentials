
words = ['one', 'two', 'three', 'four', 'five']
x = 0

print('WHILE loop:')
while (x < 5):
    print(words[x])
    x += 1

print('\nFibonacci sequence with WHILE:')
a, b = 0, 1
while (b < 1000):
    print(b, end = ' ')
    a, b = b, a + b

print()

print('\nFOR loop:')
for i in words:
    print(i)

