import _210_Modules_fibo
from _210_Modules_fibo import fib, fib2

#HIGHLIGHT: Import all names that a module defines (being able to access them directly without the module.method notation)  
#HIGHLIGHT: This imports all names except those beginning with an underscore (_)
from _210_Modules_fibo import *

    #This practice is often frowned upon, since it often causes poorly readable code.

'''
Note For efficiency reasons, each module is only imported once per interpreter session. 
Therefore, if you change your modules, you must restart the interpreter – 
or, if it’s just one module you want to test interactively, use reload(), 
e.g. reload(modulename).
'''

