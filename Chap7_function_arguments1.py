def main():
    x = 5
    print(f'in main x is {x}')
    print(f'id x is {id(x)}')
    kitten(x)
    print(f'after calling a function id x is still {id(x)}')

def kitten(a):
    print(f'id a is {id(a)}')
    a = 3
    print(f'in function a is assigned to {a}')
    print(f'id a is {id(a)}')

if __name__ == '__main__': main();
