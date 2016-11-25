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

