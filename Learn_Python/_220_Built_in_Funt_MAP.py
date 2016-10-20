'''
A quick note for Python 3 users for the Map, Reduce, and Filter functions. 
These functions return iterators in Python 3 instead of lists (as in Python 2). 
To get a list for any of these functions in Python 3, you can just cast it as a 
list using list() around the function.

Also in Python 3, reduce is imported from functools.
'''

'''
map()
map() is a function that takes in two arguments: a function and a sequence iterable. In the form: map(function, sequence)
The first argument is the name of a function and the second a sequence (e.g. a list). map() applies the function to all 
the elements of the sequence. It returns a new list with the elements changed by function.
'''

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
    
temp = [0, 22.5, 40,100]