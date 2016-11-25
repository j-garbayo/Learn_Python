'''
Generators allow us to generate as we go along, instead of holding everything in memory.

We've touch on this topic in the past when discussing the range() function in Python 2 
and the similar xrange(), with the difference being the xrange() was a generator.

We've learned how to create functions with def and the return statement. Generator functions 
allow us to write a function that can send back a value and then later resume to pick up where it left off. 

This type of function is a generator in Python, allowing us to generate a sequence of values over time.
The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal function. The main difference 
is when a generator function is compiled they become an object that support an iteration protocol.

That means when they are called in your code the don't actually return a value and then exit, the generator 
functions will automatically suspend and resume their execution and state around the last point of value generation.

STATE SUSPENSION
The main advantage here is that instead of having to compute an entire series of values upfront and the 
generator functions can be suspended, this feature is known as state suspension.
'''
'''
Defnitions of Generaror, Iterable and Iteratotor from Python Documentation

ITERABLE
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) 
and some non-sequence types like dict and file and objects of any classes you define with an __iter__() or 
__getitem__() method. Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), ...). 
When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. 
This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with 
iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. 
See also iterator, sequence, and generator.

ITERATOR
An object representing a stream of data. Repeated calls to the iterators next() method return successive items in the stream. When no more data are available a 
StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. 
Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where 
other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator
each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the
previous iteration pass, making it appear like an empty container.

GENERATOR
A function which returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop
or that can be retrieved one at a time with the next() function. Each yield temporarily SUSPENDS processing, remembering the location execution state (INCLUDING LOCAL
VARIABLES AND PENDING TRY-STATEMENTS). When the generator resumes, it picks-up where it left-off (in contrast to functions which start fresh on every invocation).

IMPORTANT!!!!
Generators generate iterators, but you can only iterate over those iterators ONCE. It's because they do not store all the values in memory, they generate the 
values on the fly and their state is not refreshed (reset) once they are exhausted.
'''

#EXAMPLES

#Gernerator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in xrange(n):
        yield num**3

for x in gencubes(10):
    print x

'''
since we have a generator function we don't have to keep track of every single cube we created.

Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don�t want to allocate the 
memory for all of the results at the same time.

As we've noted in previous lectures (such as range()) many Standard Library functions that return lists in Python 2 have been modified to return generators in 
Python 3 because generators.

Lets create another example generator which calculates fibonacci numbers:
'''

#Fibonacci generator
def genfibon(n):
    '''
    Generate fibonacci sequence up to n
    '''

    a = 1
    b = 1
    for i in xrange(n):
        yield a
        a,b = b, a+b        #HIGHLIGHT - Double assignment in a single line.

for num in genfibon(10):
    print num

#Fibonacci function

def fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

print(fibon(10))

'''
next() function
next(iterator[, default])
Retrieve the next item from the iterator by calling its next() method. If default is given, it is returned if the iterator is exhausted,
otherwise StopIteration is raised.
'''

def simple_gen():
    for x in range(3):
        yield x

#Assign simle_gen
g = simple_gen()

print g
Boolean_Test = iter(g) is g     #When applied to an iteratur, the iter() built-in function returns the same iterator WITH THE SAME STATE! (e.g. exhausted iterators)
print(Boolean_Test)             #Boolean_Test = TRUE
print next(g)
print next(g)
print next(g)
#print next(g)   #Generator is exhausted. Normally, when using an iterable such as a string, dictionary, list or tuple, the for loop captures this error
#                #and stops iteration accordingly

'''
iter()
iter(o[, sentinel])
Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument,
o must be a collection object, which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__()
method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given,
then o must be a callable object. The iterator created in this case will call o with no arguments for each call to its next() method; if the value returned
is equal to sentinel, StopIteration will be raised, oterwise the value will be returned.

One useful application of the second form of iter() is to read lines of a file until a certain line is reached. The following example reads a file until
the readline() method returns an empty string:

with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)
'''

s = 'hello' #A string, an iterable object

#Iterate over the string
for let in s:
    print let

#next(s)        #The string itself is not an iterator, but an iterable! (using next() on it raises an error)

#Nonetheless, the iter() function allows us to do just that:
s_iter = iter(s)

for i in range (len(s)):
    print (next(s_iter))

'''
Main TAKEAWAY: using the yield keywoard at a function will cause the funciton to become a generator, i.e. a function that returns an iterator.

This change can save you a lot of memoery for large use cases.
'''

'''
MORE EXAMPLES OF GENERATORS
'''

def myGen(n):
    yield n
    yield n+1

g = myGen(6)    #Yields an iterator object, which is assigned to g.

print(next(g))  #Yields 6. Stops at the line n
print(next(g))  #Yields 7. Stops at the line n+1
#print(next(g))  #This would cause an error, because the end of the iterator has been reached

for n in myGen(6):
    print(n)            #This will print 6 and 7. The for loop iterates through the iterator myGen(6).


'''
ITERTOOLS MODULE! Very important module
'''