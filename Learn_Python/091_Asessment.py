#st = 'Print only the words that start with s in this sentence'

#for word in st.split():
#    if (word[0] == "s" or word[0] == "S"):
#        print(word)

#rng = range(2,11,2)
#print(rng)

#lst = [x for x in xrange(50) if x % 3 == 0]
#print lst

st = 'Print every word in this sentence that has an even number of letters'

#for word in st.split():
#    if len(word) % 2 == 0:
#        print(word+" <-- has an even length!")

#for i in xrange(1,101):
#    if i % 3 == i % 5 == 0:
#        print "FizzBuzz"
#    elif i % 3 == 0:
#        print "Fizz"
#    elif i % 5 == 0:
#        print "Buzz"
#    else:
#        print i

st = 'Create a list of the first letters of every word in this string'

lst = [word[0] for word in st.split()]
print(lst)

st = '''| X | O | X |
-------------
|   | O | X |
-------------   
|   | O |   |'''
print(st)