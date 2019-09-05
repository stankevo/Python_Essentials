## do tuples behave like immutable when passed to a function?
## can I have values of different types inside a tuple?

def main():
    print('Questions:')
    print('1. Do tuples behave like immutable when passed to a function?')
    print('2. Can I have values of different types inside a tuple?')
    print()

    x = ('meow', 'grrr', 'purr', 1)
    print(f'id(x): {id(x)}')
    kitten(*x)

    print(f'id(x): {id(x)}')

    print()
    print('Answers:')
    print('2 - yes.')

def kitten(*args):
    print(f'id(args): {id(args)}')
    args2 = args
    print(f'id(args2): {id(args2)}')
    #args2 = ('purr', 'purr', 'purr')
    if len(args):
        for i in args2:
            print(i)
        print()
        for i in args:
            print(i)
        print()
    else:
        print('Meow.')

if __name__ == '__main__': main()

