'''
Timing your code is sometimes important to know how long your code is taking to run, or at least
to know if a particular line of code is slowing down your entire project. Python has a built-in
timing module to do this.

This module provides a simple way to time small bits of Python code. It has both a Command-Line interface
as well as a callable one. It avoids a number of common traps for measuring execution times.
'''

import timeit

#Comparison of various methods of creating the string '0-1-2-3-...-99"

#For Loop

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

#List Comprehension
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

#Map()
print(timeit.timeit('"-".join(map(str,range(100)))',number=10000))

print('end')

#Observe the significant increase in performance when using the map() function

#%TIMEIT

#iPythons %timeit will perform the code in the same line acertaain number of times (loops) and will give you the fastest
#performance time (best of 3).

#Lets repeat the above examinations:

import IPython

'''
%timeit ("-".join(str(n) for n in range(100)))

%timeit "-".join([str(n) for n in range(100)])

%timeit "-".join([str(n) for n in range(100)])
'''