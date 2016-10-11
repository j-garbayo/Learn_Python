#The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

import _210_Modules_fibo

print(dir(_210_Modules_fibo))

#Without arguments, dir() lists the names you have defined currently:
#Note that it lists all types of names: variables, modules, functions, etc.



x = 1
y = 2

print(dir())

'''
dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in 
the standard module __builtin__:
'''

import __builtin__
print(dir(__builtin__))