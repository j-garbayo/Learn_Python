import sys  

'''
sys.argv
The list of command line arguments passed to a Python script. argv[0] is the script name 
(it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line 
option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, 
argv[0] is the empty string.

To loop over the standard input, or the list of files given on the command line, see the fileinput module.
'''

'''
sys.ps1 and sys.ps2
Define the strings used as primary and secondary prompts (only applicable to the Interactive Interpreter)

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print 'Yuck!'
Yuck!
C>
'''

'''
sys.path is a list of strings that determines the interpreter's search path for modules.
It is initialized to a default path taken from the environment variable PYTHONPATH or from a built-in default
if PYTHONPATH is not set.

You can modify it using standard list operations
'''

#sys.path.append('/ufs/guiido/lib/python')