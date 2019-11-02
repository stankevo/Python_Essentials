import sys
#test2
def func():
    try:
        x = int('foo')
    except ValueError:
        print('wrong type used for int varyable "x"')

    try:
        y = 5/3 ## try to divide by zero to see how exception works
    except ZeroDivisionError:
        print('don\'t divide by zero')
    else:
        print(y) 

    try:
        z = 5/0
    except:
        print(f' An exception was caught: {sys.exc_info()[1]}')

def main():
    func()

if __name__ == '__main__': main()
