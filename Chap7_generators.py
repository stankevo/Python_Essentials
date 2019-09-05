def main():
    for i in inclusive_range(5,30,5):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    start = 0
    stop = 0
    step = 1

    numargs = len(args)
    
    #initialize parameters
    if numargs < 1:
        raise TypeError(f'Expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected at maximum 3 argument, got {numargs}')

    #generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()
