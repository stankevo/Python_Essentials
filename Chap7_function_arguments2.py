def main():
    x = [5]
    print(f'in main x is {x}')
    print(f'id x is {id(x)}')
    kitten(x)
    print(f'in main x is {x} after calling the function')
    print(f'id x is {id(x)}')


def kitten(a):
    print(f'in function id a is {id(a)}')
    a[0] = 3
    print(f'in function a is assigned to {a}')
    print(f'in function id a is {id(a)}')

if __name__ == '__main__': main()


