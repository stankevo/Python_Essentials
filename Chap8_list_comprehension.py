def main():
    print("1. Create a list wich consists of elements of the other list which are multiplied by 2.")
    l1 = range(11)
    l2 = (i*2 for i in l1)
    print_list(l1)
    print_list(l2)

    print("\n2. Create a list which consists of elements of the other list that are not dividable by 3.")
    l3 = (i for i in l1 if i % 3 != 0)
    print_list(l1)
    print_list(l3)

    print("\n3. Create a list of tuples where one element is a figure and the other element is a squared of this figure.")
    l4 = [(i, i**2) for i in l1]
    print_list(l4)

    print("\n4. Create a list of pi values rounded to 0, 1, .., 10.")
    from math import pi
    l5 = [round(pi, i) for i in l1]
    print_list(l5)

    print("\n5. Create a dictionary: key is the digit, value is the squared digit.")
    d = {i: i**2 for i in l1}
    print(d)

    print("\n6. Create a set of letters which are in phrase 'superduper' and are not in string 'pd'")
    s = {i for i in 'superduper' if i not in 'pd'}
    print_list(s)

def print_list(o):
    for i in o: print(i, end=' ')
    print()

if __name__ == '__main__': main()