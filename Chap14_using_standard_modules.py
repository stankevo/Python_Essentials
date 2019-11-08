# sys
import sys

v = sys.version_info
print(v)
print('Python version is {}.{}.{}'.format(*v))

# os
import os
s = os.name
print(f'\n{s}')

p = os.getenv('PATH')
print(f'\nPATH = {p}')

d = os.getcwd()
print(f'\nCurrent working directory is {d}')

r = os.urandom(10)
print(f'\nrandom value from OS is {r}')
print(f'random value from OS is {r.hex()} (hex)')

# random
import random

x = random.randint(1,1000)
print()
print(x)

l = list(range(1,25))
print()
print(l)
random.shuffle(l)
print(l)

# datetime
import datetime

now = datetime.datetime.now()
print()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

