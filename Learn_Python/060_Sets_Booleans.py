'''
Sets are an unordered collection of UNIQUE (NO REPETITIONS) elements. 
We can construct them by using the set() function. 
Let's go ahead and make a set to see how it works
Sets are not dictionaries, although you can draw analogies as a set being a dictionary with only keys.
'''

x = set()

# We add to sets with the add() method
x.add(1)
print(x)

# Add a different element
x.add(2)
print(x)

# Try to add the same element
x.add(1)
print(x)

#THE SET IS ONLY CONCERNED WITH UNIQUE ELEMENTS! (NO REPETITIONS)

#cast a list with multiple repeat elements to a set to get the unique elements. 
l = [1,1,2,2,3,4,5,6,1,1]
print(set(l))

a = True
print(a)

#We can also use comparison operators to create booleans.
b = 1 > 2   #b is a boolean
print(b)