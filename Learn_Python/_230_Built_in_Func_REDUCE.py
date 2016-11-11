'''
If seq = [ s1, s2, s3, ... , sn ], calling reduce(function, sequence) works like this:

- At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
- The list on which reduce() works looks now like this: [ function(s1, s2), s3, ... , sn ]
- In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
- The list looks like this now: [ function(function(s1, s2),s3), ... , sn ]
- It continues like this until just one element is left and return this element as the result of reduce()

Lets see an example:
'''

lst =[47,11,42,13,14,16]
reduce(lambda x,y: x+y,lst)
