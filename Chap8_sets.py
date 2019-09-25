def main():
    a = set("We're gonna need a bigger boat.")
    b = set("Im sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    
    print()
    print_set(sorted(a))
    print_set(sorted(b))

    print()
    print('Items which are in a but not in b')
    print_set(a - b)

    print()
    print('Items which are in a or in b')
    print_set(a | b)

    print()
    print('Items which are in a or in b, but not in both')
    print_set(a ^ b)

    print()
    print('Items which are in a and in b')
    print_set(a & b)

def print_set(s):
    print('{', end = '')
    for i in s: print(i, end = '')
    print('}')

if __name__ == '__main__': main()