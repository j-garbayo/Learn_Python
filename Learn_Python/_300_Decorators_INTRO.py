'''
This is an introductory to the syntax of decorators. It has no intention to be an in depth coverage.

Decorators are heavily used in the web frameworks FLISK and DJANGO.
'''

#SCOPE Review: remember from the nested statements that ython uses Scope to know what a label is referring to. F.e:

s = 'Global Variable'
def func():
    print locals()

print globals().keys() #Retains only the keys of the dictionary of all the global variables.
    #'s' is within that dictionary

print globals()['s']

#Executing func() shows that the local variables of this function is an empty dictionary.
func()

'''
Assign a label to a function (functions as object)
'''

def hello(name='Jose'):
    return 'Hello ' + name

#Execute the function (use brackets at the end)
print(hello())

#Assign a label to a function (use no parenthesis)
greet = hello

#Get the address of the label
print(greet)

#Execute the labelled function
print(greet())

#The assignment is not attached to the original function!
del hello   #deletes hello from the namespace, effectively deleting the function
#hello()     #Now this would yield an error
greet()     #This works still, regardless of whether hello was deleted. Greet is an independent instance?
del greet

'''
Functions within functions
'''

def hello(name='Jose'):
    print 'The hello() function has been executed'

    def greet():
        #HIGHLIGHT - use \t in a string to introduce a tab command
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'

    print greet()
    print welcome()
    print 'Now we are back inside the hello() function'

hello()

#welcome()   #This would yield an error because the function 'welcome' exists only within the scope of the function hello

'''
Functions that return functions within them
'''

def hello(name = 'Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'

    if name == 'Jose':
        return greet
    else:
        return welcome

function_1 = hello()
print(function_1)   #Note how function 1 is now a label assigned to the function 'greet' defined within the function 'hello'
print(function_1()) #function_1 executes is a label within the namespace of global variables that executes the greet function within 'hello'

del hello
del function_1

'''
Functions that accept functions as arguments
'''

def hello():
    return 'Hi Jose'

def other(func):
    print 'Other code would go here'
    print func()

other(hello)

del hello
del other

'''
Syntax equivalet to a decorator
'''
def new_decorator(func):

    def wrap_func():
        print 'Code to be executed before the func would be here'

        func()

        print 'Code to be executed after the funct would be here'

    return wrap_func

def func_needs_decorator():

    print 'This function is in need of a decorator'

#Executing func_needs_decorator
func_needs_decorator()

#Reassing func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)
print(func_needs_decorator)     #Now the label 'func_needs_decorator' has been effectively assigned to 'wrap_func'

#Executing the function now is calls the wrap_func
func_needs_decorator()

del func_needs_decorator
del new_decorator

'''
Using decorators syntax
'''

print ""
print "Using decorators syntax"
print ""

def new_decorator(func):

    def wrap_func():
        print 'Code to be executed before the func would be here'

        func()

        print 'Code to be executed after the funct would be here'

    return wrap_func

#Internally, the syntax below has the same effect as the following - passing the function through the decorator and assigning the result back 
#to the original name:

@new_decorator      #same as func_needs_decorator = new_decorator(func_needs_decorator)
def func_needs_decorator():
    print 'This function is in need of a Decorator'

print(func_needs_decorator)     #Because of the use of the decorator syntax, the label 'func_needs_decorator' points to wrap_func
                                #to which the original 'func_needs_decorator' has been passed as an argument.

func_needs_decorator()

def func_needs_decorator_2():
    print 'This function also needs a Decorator'

needs_decorator = func_needs_decorator_2

'''
From Learning Python - A Fisrt Look at User-Defined Function Decorators
'''

#Recall from Chater 30 that the __call__operator overloading method imlements a function-call interface for class instances (ver mi ejemplo)
#The example below uses this to define a call proxy class that saves the decorated function in the instance and catches calls to the original
#name. Because this is a class, it also has state information - a counter of calls made.

class tracer:
    def __init__(self,func):    # Remember original, init counter
        self.calls = 0
        self.func = func

    def __call__(self, *pargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*pargs)

@tracer                             #same as spam = tracer(spam) - spam becomes an instance of "tracer" with self.func = 'the original spam'
def spam(a,b,c):                    #Wrap spam in a decorator object
    return a + b + c

print(spam)
print(spam(1,2,3))      # Really calls the tracer wrapper object
print(spam('a','b','c'))

print('Spam has been called ' + str(spam.calls) + ' times')

#The decorator above does not handle 'Keyword' arguments
#The decorator above cannot decorate class-level method functions (for methods, its __call__ would be passed a tracer instance only).

#Part VIII of the learning Python book explains decorators in detail.
#Alternatives such as using def nested statements for decorators are better suited to decorate methods than the previous example.

def tracer2(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0    #Initializces oncall.calls when 'func' is wrapped
    return oncall       #thanks to this, the @tracer2 sentence wraps the function with 'oncall'

class Csample:
    @tracer2                #same as spam = tracer2(spam)
    def spam(self, a, b, c): return a + b + c

x = Csample()
print x.spam    #since the spam method is wrapped by tracer2, the result is that the spa label here is assigned to oncall.
print(x.spam(1,2,3))
print(x.spam('a','b','c'))

