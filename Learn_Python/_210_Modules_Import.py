import _210_Modules_fibo
from _210_Modules_fibo import fib, fib2

#HIGHLIGHT: Import all names that a module defines (being able to access them directly without the module.method notation)  
#HIGHLIGHT: This imports all names except those beginning with an underscore (_)
from _210_Modules_fibo import *

    #BAD PRACTICE
    #This practice is often frowned upon, since it often causes poorly readable code
    #It also can cause main program and imported module names to clash

#HIGHLIGHT: Import 'as'
from math import sqrt as square_root
print(square_root(100))

'''
Note For efficiency reasons, each module is only imported once per interpreter session. 
Therefore, if you change your modules, you must restart the interpreter � 
or, if it�s just one module you want to test interactively, use reload(), 
e.g. reload(modulename).
'''

