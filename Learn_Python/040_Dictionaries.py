#Normal Dictionary
d = {'k1':1,'k2':2}

#Dictionary Comprehensions
{x:x**2 for x in range(10)}

#Iteration over keys
for key in d:
    print key

for key in d.iterkeys():
    print key

#Iteration over values
for value in d.itervalues():
    print value

#Iteration over keys and values
for k, v in d.iteritems():
    print k, v
