# fix: 20: twenty-zero

class numToWord:
    def __init__(self, n = None):
        self._number = n
        self._word = 'None'

        self._dict20 = {
            0: 'zero',      1: 'one',        2: 'two',       3: 'three',     4: 'four', 5: 'five', 
            6: 'six',       7: 'seven',      8: 'eight',     9: 'nine',     10: 'ten',
            11: 'eleven',  12: 'twelve',    13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

        self._dictTens = {
            20: 'twenty', 30: 'thirty', 40: 'fourghty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}

        self._word = self.getword(n)


    def __repr__(self):
        return f'{self._word}'

    def number(self, n = None):
        if n: self._number = n
        return self._number

    def word(self):
        return self._word

    def getword(self, n):
        if n >= 0 and n <= 19:
            w = self._dict20[n]
        elif n < 100:
            a = (n // 10) * 10
            b = n % 10
            w = self._dictTens[a] + '-' + self._dict20[b] 
        return w

def main():
    a = numToWord(79)
    print(a)
    b = a.number()
    c = a.word()
    print(b, a)

    for i in range(100):
        print(f'{i}: {numToWord(i)}')
    

if __name__ == '__main__': main()