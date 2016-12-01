'''
Built-in Module that implements specialized container data types, providing alternatives to Python's
general purpose built-on containers. We've already gone over the basics: dict, list, set and tuple.

Now we'll learn about the alternatives that the collections module provides
'''

#COUNTER

#Counter is a dict subclass, which helps count hash-able objects. Inside of it, elements are stored
#as dictionary keys and the counts of the objects are stored as the value

from collections import Counter

#Counter with lists

l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

counter_l = Counter(l)
print(counter_l)

#Counter with strings

l = 'aabsbsbsbhshhbbsbs'

counter_l = Counter(l)
print(counter_l)

#Counter with words in a sentence

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
counter_words = Counter(words)
print (counter_words)

#Common patterns using the counter object:

#sum(c.values())                 # total of all counts
#c.clear()                       # reset all counts
#list(c)                         # list unique elements
#set(c)                          # convert to a set
#dict(c)                         # convert to a regular dictionary
#c.items()                       # convert to a list of (elem, cnt) pairs
#counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
#c.most_common()[:-n-1:-1]       # n least common elements
#c += counter()                  # remove zero and negative counts


#DEFAULT DICT

#defaultdict is a dictionary like object which provides all methods provied by a dictionary but takes first argument
#(default_factory) as a callable which returns the default data type for the dictionary. Using defaultdict is faster 
#than doing the same using dict.set_default method.

#A DEFAULTDICT WILL NEVER RAISE A KEYERROR. ANY KEY THAT DOES NOT EXIST GETS THE VALUE RETURNED BY THE CALLABLE DEFAULT_FACTORY

from collections import defaultdict

d = {}  #normal dictionary
#print(d['one'])    #This would raise a KeyError, since this is a normal dictionary

#Use of defaultdict with an object as 'default_factory'. An object is a 'callable'
d = defaultdict(object)
print(d['one'])     #This does not raise a KeyError, because we are working with a defaultdict

#Can also initialize with default values
d = defaultdict(lambda: 0)      #This does not raise a KeyError, because we are working wit a defaultdict.
print(d['one'])

#ORDERED DICTIONARY

#An OrderedDict is a dictionary subclass that remembers the order in which it contents are added.

#Example of a normal dictionary

from collections import OrderedDict

print 'Normal dictionary:'

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print k, v

print 'OrderedDict:'

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

#Equality with an Ordered Dictionary:
#It does not only test the items of the dictionary, but also the order in which they were added.

print 'Dictionaries (normal) are equal?'

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'Dictionaries (ordered) are equal?'

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

#NAMED TUPLE

#The standafrd tuple uses numerical indexes to access its members, for example:

t = (12,13,14)

print (t[0])

#For simple use cases, this is usually enough. On the other hand, remembering which index should be used for each value can lead to errors, 
#especially if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names, as well as the numerical 
#index, to each member.

#Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. The arguments are the name of the 
#new class and a string containing the names of the elements.
#You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields. For example:

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab',name='Sammy')
frank = Dog(age=2, breed='Shepard',name='Frankie')

print "namedtuple('Dog', 'age breed name')"

print 'sam'
print sam

print 'sam.age'
print sam.age

print 'sam.breed'
print sam.breed

print 'sam[0]'
print sam[0]

