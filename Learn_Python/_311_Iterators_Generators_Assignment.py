'''
PROBLEM 1
Create a generator that generates the squares of numbers up to some number N.
'''



def gensquares(N):
    for i in xrange(N):
        yield i**2

print('gensquares(10)')

for x in gensquares(10):
    print x

print('')

'''
PROBLEM 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:
'''

import random

def rand_num(low,high,n):
    for i in xrange(n):
        yield random.randint(low, high)

print('rand_num(1,10,12)')

for num in rand_num(1,10,12):
    print num

print('')

'''
PROBLEM 3
Use the iter() function to convert the string 's'
'''

s = 'hello'

iter_s = iter(s)

print('iter_s')

for i in xrange(len(s)):
    print next(iter_s)

print('')