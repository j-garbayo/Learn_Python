import sys

'''
HIGHLIGHT - THE MODULE SEARCH PATH

When a module named spam is imported, the interpreter first searches for a built-in module with that name. 
If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. 
sys.path is initialized from these locations:

the directory containing the input script (or the current directory).
PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
the installation-dependent default.

After initialization, Python programs can modify sys.path. The directory containing the script being 
run is placed at the beginning of the search path, ahead of the standard library path. This means 
that scripts in that directory will be loaded instead of modules of the same name in the library 
directory. This is an error unless the replacement is intended.
See section Standard Modules for more information.
'''

print(sys.path)