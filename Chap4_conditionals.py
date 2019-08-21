if False:
    print('first')
elif True:
    print('elif 1')
elif False:
    print('elif 2')
else:
    print('nothing from above')
print()


x = 4
print('x = 4')
if x == 0:
    print('x is 0')
elif x == 1:
    print('x is 1')
elif x == 2:
    print('x is 2')
elif x == 3:
    print('x is 3')
elif x == 4:
    print('x is 4')
else:
    print('x is not in (1,2,3,4)')
print()


x = 42
print('x = 42')
if x == 0:
    print('x is 0')
elif x == 1:
    print('x is 1')
elif x == 2:
    print('x is 2')
elif x == 3:
    print('x is 3')
elif x == 4:
    print('x is 4')
else:
    print('x is not in (1,2,3,4)')
print()

print('Conditional assignment:')
hungry = 0
y = 'Feed the bear now!' if hungry else 'Do not feed the bear now.'
print(y)


