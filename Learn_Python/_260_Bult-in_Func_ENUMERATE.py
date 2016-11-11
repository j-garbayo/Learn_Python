'''
Enumerate allows you to keep a count as you iterate through an object. It does this by returning an enumerate object (which is a generator object) containing a count, element 
correspondence in the form (count, element). See the examples her from the book "Learning Python for futher clarification".

The function itself is equivalent to:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
'''

lst = ['a','b','c']

#The following print shows that enumerate has its own object structure. It is not a list of tuples as "ZIP":
print (enumerate(lst))

for number, item in enumerate(lst):
    print number, item

#Enumerate becomes particularly useful when you have a case where you need to have some sort of tracker. For example:

for count, item in enumerate (lst):
    if count >= 2:
        break
    else:
        print count, item

#Further examples from the "Learning Python book":
S = 'spam'
for offset, item in enumerate(S):
    print item, 'appears at offset', offset

'''
HIGHLIGHT - Enumerate
FROM BOOK LEARNING PYTHON
The enumerate funciton returns a 'GENERATOR OBJECT' - a kind of object that supports the iteration protocol that we will study un chapter 14 and
will discuss in more detail in the next part of the book. 

In short, it has a method called by the 'next' built-in function, which returns an (index, value) tuple each time through the loop. The 'for'
steps through these tuples automatically, which allows us to unpack their values with tuple assignment much as we did for 'zip':

The lines below show the machinery we do not normally use:
'''

E = enumerate(S)
print(E)
print(next(E))
print(next(E))
print(next(E))
print(next(E))

'''
HIGHLIGHT - Turn an Enumerate object into a list of tuples using the method 'list()'
The method list() takes sequence types and converts them to lists. This is uded to convert a given tuple into a list.
It can also be used to convert an enumerate method into a list of its tuples. See below:
'''

Elist = list(enumerate(S))
print (Elist)






