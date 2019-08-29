
pets = ('cat', 'dog', 'fish', 'hamster', 'velociraptor')

for i in pets:
    if i == 'dog': continue
    print(f'- {i}')
else:
   print('These are all pets.')
