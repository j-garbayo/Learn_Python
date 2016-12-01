x = [1,3,4]
y = 2
z = 3

result = y + z
print result

import pdb

#Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x       #This line would raise an error because there is no operation defined to sum or concatenate lists and integers
print result2

'''
For more information on general debugging techniques and more methods, check out the official documentation:
https://docs.python.org/2/library/pdb.html
'''