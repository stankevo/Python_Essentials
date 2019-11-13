import datetime

class numToWord:
    def __init__(self, n = None):
        self._number = n
        self._word = 'None'

        self._dict20 = {
            0: 'zero',      1: 'one',      2: 'two',        3: 'three',     4: 'four', 
            5: 'five',      6: 'six',      7: 'seven',      8: 'eight',     9: 'nine',
            10: 'ten',     11: 'eleven',  12: 'twelve',    13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

        self._dictTens = {
            20: 'twenty', 30: 'thirty',  40: 'forty',  50: 'fifty',
            60: 'sixty',  70: 'seventy', 80: 'eighty', 90: 'ninety'}

        self._word = self._getword(n)

    def __repr__(self):
        return f'{self._number} - {self._word}'

    def number(self, n = None):
        if n: self._number = n
        return self._number

    def word(self):
        return self._word

    def _getword(self, n):
        if n < 0 or n >= 100:
            raise TypeError(f'Expected value between 0 and 99, got {n}.')
        if n >= 0 and n <= 19:
            w = self._dict20[n]
        elif n % 10 == 0:
            w = self._dictTens[n]
        else:
            a = (n // 10) * 10
            b = n % 10
            w = self._dictTens[a] + '-' + self._dict20[b]
        return w

def main():
    x = 1
    try:
        a = numToWord(x)
        print(a)
        b = a.number()
        c = a.word()
        print(b, c)
    except TypeError as e:
        print(f'Error: {e}')
    # test
  ##  for i in range(100):
  ##      print(f'{i}: {numToWord(i).word()}')

    now = datetime.datetime.now()

    try:        
        tw = timeToWord(now.time())
        print(tw)
    except TypeError as e:
        print(f'TypeError: {e}')

class timeToWord:
    def __init__(self, t = None):
        if isinstance(t, datetime.time): 
            self._time = t
            self._hour = t.hour
            self._minutes = t.minute
        else: raise TypeError(f'timeToWord expects a value of type datetime.time as an agrument, got {type(t)}.')

    def __repr__(self):
        return f'time: {self._time}, hour: {self._hour}, minutes: {self._minutes}'

      
if __name__ == '__main__': main()