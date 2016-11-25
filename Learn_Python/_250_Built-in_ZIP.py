'''
zip() makes an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The iterator stops when the shortest input iterable is exhausted.
With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

zip() is equivalent to:
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

zip() should only be used with unequal length inputs when you don�t care about trailing, unmatched values from the longer iterables.
'''

#See the one note notebook for futher details.
#The function could also be written.

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

print(zip(x,y,z))

a = [1,2,3,4,5]
b = [2,2,10,1,1]

#Using ZIP to return the greatest of this two elements:
print(map(lambda pair: max(pair), zip(a,b)))

#ZIP with dictionaries
#By default
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

print(zip(d2,d1.itervalues()))

#Swap the elements of each dictionary

def switcharoo(d1,d2):

    dout = {}

    for d1key, d2val in zip(d1, d2.itervalues()):
        dout[d1key] = d2val

    return dout

print(switcharoo(d1,d2))