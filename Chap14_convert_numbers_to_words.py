class numword:
    def __init__(self, n):
        self._number = n

    def __repr__(self):
        return f'{self._number}'

    def number(self):
        return self._number

def main():
    a = numword(5)
    print(a)
    b = a.number()
    print(b)
    

if __name__ == '__main__': main()