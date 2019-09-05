def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow')
    #return dict(Alza = 'Meow', Bonbon = 'Purr')
    return {'Alza': 'Meow', 'Bonbon': 'Purr'}

if __name__ == '__main__': main()