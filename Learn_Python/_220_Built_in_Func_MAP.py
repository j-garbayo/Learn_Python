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
    
#temp = [0, 22.5, 40,100]

##Conversion to Fahrenheit
#F_temps = map(fahrenheit, temp)
#print(F_temps)

##Return to celsius
#F_temps = map(celsius, F_temps)
#print(F_temps)

'''map and lampda expressions'''
temp = [0, 22.5, 40,100]
F_temps = [32.0, 72.5, 104.0, 212.0]
F_temps = map(lambda x: (5.0/9)*(x - 32), F_temps)

print(F_temps)

'''
map() can be applied to more than one iterable. The iterables have to have the same length.
For instance, if we are working with two lists-map() will apply its lambda function to the elements of the argument lists, 
i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached.
For example lets map a lambda expression to two lists:
'''

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(map(lambda x,y:x+y, a,b))
print(map(lambda x,y,z:x+y+z, a,b,c))