def f1():
    print('call function f1().')

x = f1
x()

print('--------------------------------------------')
print('Part2:')

def ff1():
    def ff2():
        print('call function ff2().')
    return ff2

##ff2()  - this will not work as ff2() is defined only in scope of ff1()
y = ff1() # here we should use ff2() with '()', because we want assign to x not the ff1 function, but what this function returns.
y()

print('--------------------------------------------')
print('Part3:')


def a1(f):

    def a2():
        print('before calling the function')
        f()
        print('after calling the function')
        print()

    return a2

@a1
def a3():
    print('function a3() is called.')

@a1
def a4():
    print('function a4() is called.')

def a5():
    print('function a5() is called.')

a3()
a4()

## benefits of decorators:
# - we can whrap several different functions into a one wrapper: different logic, but same formatting
# - we are hiding the logic, so it can be called only with appropriate wrap

print('same done without decorator syntax:')
b = a1(a5)
b()
# or, to hide name a5():
a5 = a1(a5)
a5()



