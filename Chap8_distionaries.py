def main():
    print("1. create a dictionary")
    print("print a dictionary via iterating")
    animals1 = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
                'girafe': 'I am a giraffe!', 'dragon': 'rawr'}
    print_dict1(animals1)

    print("\n2. create a dictionary via constructor")
    print("\nprint a dictionary via items() method")
    animals = dict(kitten= 'meow', puppy= 'ruff!', lion= 'grrr',
                   girafe= 'I am a giraffe!', dragon= 'rawr')
    print_dict(animals)

    print("\n3. print only keys")
    print(animals.keys())

    print("\n4. print only values")
    print(animals.values())

    print("\n5. pick an element using its key")
    print(animals['dragon'])

    print("\n6. assign a different value for an element")
    animals['lion'] = 'I am a lion!'
    print_dict(animals)

    print("\n7. add a new item")
    animals['monkey'] = 'ahaha'
    print_dict(animals)

    print("\n8. search for a key using in operator + a conditional expression")
    print('Yes' if 'lion' in animals else 'Nope')
    print('Yes' if 'godzilla' in animals else 'Nope')

    print("\n9. try to return a values if you don't know if the key exists, but you do not want an exception' (don't use in)")
    print(animals.get('monkey'))
    print(animals.get('godzilla'))

def print_dict1(d):
    for i in d: print(f'{i}: {d[i]}')

def print_dict(d):
    for k, v in d.items(): print(f'{k}: {v}')


if __name__ == '__main__': main() 