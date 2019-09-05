def main():
    x = dict(Alza = 'Meow', Zuza = 'Purr', Panny = 'Grrr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print('{} says "{}"'.format(i, kwargs[i]))
    else:
        print('Meeeoooow.')

    print()

    kwargs["Alza"] = "I'm hungry!"
    if len(kwargs):
        for i in kwargs:
            print('{} says "{}"'.format(i, kwargs[i]))
    else:
        print('Meeeoooow.')


if __name__ == '__main__': main()
