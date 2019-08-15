#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 41
print('Hello, World. {} 1'.format(x))

x = 42
y = 'Hello, World. {} 2'.format(x)
print(y)

x = 43
print(f'Hello, World. {x} 3')

x = 44 #Python 2
print('Hello, World. %d 4' % x)