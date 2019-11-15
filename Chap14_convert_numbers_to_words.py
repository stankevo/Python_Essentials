# bug: 00:01:00 - fifty-nine past midnight

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


class timeToWord:
    def __init__(self, t = None):
        if isinstance(t, datetime.time): 
            self._time = t
            self._hour = t.hour
            self._minutes = t.minute
        else: raise TypeError(f'timeToWord expects a value of type datetime.time as an agrument, got {type(t)}.')
        
        self._tword = self._getWordFromTime(self._hour, self._minutes)
    
    def _hourToWord(self, h):
        if h == 0:
            w = 'midnight'
        elif h == 12:
            w = 'noon'
        else:
            w = numToWord(h % 12).word()
        return w

    def _minToWord(self, m):
        if m == 15:
            w = 'quarter'
        elif m == 30:
            w = 'half'
        else:
            w = numToWord(m).word()
        return w


    def _getWordFromTime(self, hour, minutes):
        wHour = self._hourToWord(hour)
        nextHour = 0 if hour == 23 else hour + 1
        wNextHour = self._hourToWord(nextHour)
        rMinutes = 60 - minutes

        wMinutes = self._minToWord(minutes)
        rMinutes = 60 - minutes
        wrMinutes = self._minToWord(rMinutes)

        if minutes == 0:
            wTime = wHour if (hour % 12) == 0 else  wHour + " o'clock" 
        elif minutes <= 30:
            wTime = wMinutes + ' past ' + wHour
        else:
            wTime = wrMinutes + ' till ' + wNextHour
        return wTime


    def __repr__(self):
        return self._tword


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
    #  for i in range(100):
    #      print(f'{i}: {numToWord(i).word()}')

    now = datetime.datetime.now()

    try:        
        tw = timeToWord(now.time())
        print(tw)
    except TypeError as e:
        print(f'TypeError: {e}')

    # test time
    t1 = datetime.time(0,0)
    t2 = timeToWord(t1)
    print(t2)

    l = ((0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
             (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
             (23, 59), (12, 59), (13, 59)
            )

    tests = list()
    for i in l:
        tests.append(datetime.time(i[0], i[1]))

    for i in tests:
        print(f'{i} - {timeToWord(i)}')



if __name__ == '__main__': main()