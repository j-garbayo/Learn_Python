#TUPLE UNPACKING

#It only works if all the tuples are equally sized!

l = [(2,4),(6,8),(10,12)]

for tup in l:
    print tup

for (t1,t2) in l:
    print (t2)

#For example, now it wouldnt work

#l = [(2,4),(6,8),(10,12,13)]

#for (t1,t2) in l:
#    print (t2)

#DICTIONARIES ITERATION

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print item

#d.iteritems() creates a generator that generates the keys and values of the dictionary.
print("")
print(".iteritems()") 
for (k,v) in d.iteritems():
    print ("k = " + str(k))
    print ("v = " + str(v))

#Alternatively d.items() returns a list of tuples through which we can iterte using tuple unpacking
#HOWEVER: THIS CAN POTENTIALLY USE A LOT OF MEMORY, SO ITS BAD PRACTICE
#IN PYTHON3, ITEMS IS ALREADY A GENERATOR, OR AT LEAST DOES NOT INVOLVE MEMORY PROBLEMS
print("")
print(".items()") 
for (k,v) in d.items():
    print ("k = " + str(k))
    print ("v = " + str(v))

#EXPLANATION
'''
You might be wondering why this worked in Python 2. This is because of the introduction of
generators to Python during its earlier years. (We will go over generators and what they are in a
future section, but the basic notion is that generators don’t store data in memory, but instead just
yield it to you as it goes through an iterable item).
Originally, Python items() built a real list of tuples and returned that. That could potentially
take a lot of extra memory.
Then, generators were introduced to the language in general, and that method was reimple-
mented as an iterator-generator method named iteritems(). The original remains for backwards
compatibility.
One of Python 3’s changes is that items() now return iterators, and a list is never fully built.
The iteritems() method is also gone, since items() now works like iteritems() in Python 2.
'''

#x = 0

#while x < 10:
#    print 'x is currently: ',x
#    print ' x is still less than 10, adding 1 to x'
#    x+=1

x = 0

#while x < 10:
#    print 'x is currently: ',x
#    print ' x is still less than 10, adding 1 to x'
#    x+=1
#    if x ==3:
#        print 'x==3'
#        break
#    else:
#        print 'continuing...'
#        continue

x = range(0,10) #THE TOTAL NUMBER OF ELEMENTS IS END - START. THE ELEMENT 10 IS NOT INCLUDED
print(type(x))
print(x)

# Grab every letter in string
lst = [x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]

print(fahrenheit)

