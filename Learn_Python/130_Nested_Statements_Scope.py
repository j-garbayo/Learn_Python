x = 25

def printer():
    x = 50
    return x

print x
print printer()

'''
In simple terms, the idea of scope can be described by 3 general rules:

1. Name assignments will create or change local names by default.
2. Name references search (at most) four scopes, these are:
    * local
    * enclosing functions
    * global
    * built-in
3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
'''

'''
The statement in #2 above can be defined by the LEGB rule.

**LEGB Rule.**

L: Local � Names assigned in any way within a function (def or lambda)), and not declared global in that function.

E: Enclosing function locals � Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) � Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) � Names preassigned in the built-in names module : open,range,SyntaxError,...
'''

#Local
# x is local here:
f = lambda x:x**2

#Enclosing Functions Local
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print 'Hello '+name
    
    hello()

print(name)
greet()

#GLOBAL (vs Local)
x = 50

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

func(x)
print 'x is still', x

#BUILT IN
len

#THE GLOBAL STATEMENT

'''
If you want to assign a value to a name defned at the top level of the program (i.e. not inside
any kind of scope such as functions or classes), then you have to tell Python that the name is not
local, but it is global. We do this using the global statement. It is impossible to assign a value to a
variable de?ned outside a function without the global statement.

You can use the values of such variables de?ned outside the function (assuming there is no
variable with the same name within the function). 

However, this is not encouraged and should be avoided since it becomes unclear to the reader of the 
program as to where that variable�s de?nition is. Using the global statement makes it amply clear that 
the variable is de?ned in an outermost block.
'''

x = 50

def func():
    global x
    y = 2   #This is a local variable
    print 'This function is now using the global x!'
    print 'Because of global x is: ', x
    x = 2
    print 'Ran func(), changed global x to', x
    b = locals()
    print('locals ',b)

print 'Before calling func(), x is: ', x
func()
print 'Value of x (outside of func()) is: ', x

#GLOBALS()
'''
Return a dictionary representing the current global symbol table. This is always the dictionary 
of the current module (inside a function or method, this is the module where it is defined, not 
the module from which it is called).
'''
a = globals()

#LOCALS()


