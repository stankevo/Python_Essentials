class InclusiveRange:
    def __init__(self, *args):
        numArgs = len(args)
        self._start = 0
        self._step = 1

        if numArgs < 1:
            raise TypeError(f'The InclusiveRange() expects at list one argument, got {numArgs}.')
        elif numArgs == 1:
            self._stop = args[0]
        elif numArgs == 2:
            (self._start, self._stop) = args
        elif numArgs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'The InclusiveRange() expects maximum 3 arguments, got {numArgs}')

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        x = self._next
        self._next += self._step
        if self._next <= self._stop + 1:
            return x
        else: 
            raise StopIteration

def main():
    for i in InclusiveRange(5):
        print(i, end=' ')
    print()

    for i in InclusiveRange(5,25):
       print(i, end=' ')
    print()

    for i in InclusiveRange(5,25,5):
       print(i, end=' ')
    print()

if __name__ == '__main__': main()
