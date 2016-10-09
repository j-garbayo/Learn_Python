'''
In Python tuples are very similar to lists, however, unlike lists they are *immutable* meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar. 

In this section, we will get a brief overview of the following:

    1.) Constructing Tuples
    2.) Basic Tuple Methods
    3.) Immutability
    4.) When to Use Tuples.

You'll have an intuition of how to use tuples based on what you've learned about lists. We can treat them very similarly with the major distinction being that tuples are immutable.

## Constructing Tuples

The construction of a tuples use () with elements separated by commas. For example:
'''

# Can create a tuple with mixed types
t = (1,2,3)

# Check len just like a list
print(len(t))

# Can also mix object types
t = ('one',2)

# Show
print("t = " + str(t))

# Use indexing just like we did in lists
print(t[0])

# Slicing just like a list
print "t[-1]"
print(t[-1])

#Test combination of tuples and lists
test_tuple = (1,2,[1,2])
print("test_tuple = " + str(test_tuple))
print "Now we execute 'test_tuple[2].append(4)'"
test_tuple[2].append(4)
print("test_tuple = " + str(test_tuple))
test_tuple[2][2] = 5
print("test_tuple = " + str(test_tuple))

print("")
print("BASIC TUPLE METHODS")

# Use .index to enter a value and return the index
print("t.index('one') = " + str(t.index('one')))

# Use .count to count the number of times a value appears
print("t.count('one') = " + str(t.count('one')))

