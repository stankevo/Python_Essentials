class inclusive_range:
    def __init__(self, *args):
        self._start = 0
        self._step = 1

        if len(args) < 1:
            raise TypeError(f'Wrong number of attributes for inclusive_range(): expected at list 1, got {len(args)}.')
        elif len(args) == 1:
            self._stop = args[0]
        elif len(args) == 2:
            (self._stop, self._step) = args
        elif len(args) == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'Wrong number of attributes for inclusive_range(): expected at most 3, got {len(args)}.')

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

        

def main():
    try:
        for i in inclusive_range(1,1,1,1):
            print(i, end=' ')
    except TypeError as e:
        print(f'Rage error: {e}')

if __name__ == '__main__': main()