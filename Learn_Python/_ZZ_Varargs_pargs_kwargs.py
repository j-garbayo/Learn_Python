'''
This intends to clarify the use of * and ** in function headers and function calls

This introduces practical examples. The theory is from chapter 18 of the book. The onenote book makes also a summary
'''

'''
DEFINITIONS: POSITIONAL VS KEYWORD ARGUMENTS

- Positional Arguments (functions): matched from left to right.
    - the normal case is to match passed argument values to argument names in a function header by position, from
      left to right.

- Keyword arguments (functions): matched by argument name.
    - Alternatively, callers can specify which argument in the function is to receive a value by using the argument's name in the call,
      with the name=value syntax

- Keyword only arguments: arguments that must be passed by name.
    - In Python 3.X (not in 2.X), functions can aslo specify arguments that must be passed by name with keyword arguments, not by position.
      Such arguments are typically used to define configuration options in addition to actual arguments.
'''

'''
VARARGS COLLECTING AND VARARGS UNPACKING

    - Varargs coolecting: collect arbitrarily many positional or keyword arguments:
        - Functions can use special arguments preceded with one or two * characters to collect an arbitrary number of possibly extra arguments.
          This feature is often referred to as varargs, after a variable-length argument list tool in the C language; in Python, the arguments
          collected in a normal object.

    - Varargs unpacking: pass arbitrarily many positional or keyword arguments
        - Callers can also use the * syntax to unpack argument collections into separate arguments. This is the inverse of a * in a function
          header. In the header it means collect arbitrarily many arguments, while in the call it means unpack arbitrarily many arguments, and
          ass them individually as discrete values
'''

'''
ARGUMENT MATCHING SYNTAX

    SYNTAX                LOCATION          MEANING        
    func(*name)           caller            Pass all objects in iterable as individual positional arguments
    func(**dict)          caller            Pass all key/value pairs in dict as individual keyword arguments
    func(*name)           Function          Matches and collects remaining positional arguments in a tuple
    func(**dict)          Function          Matches and collects remaining keyword arguments in a dictionary
    funct(*other, name)   Function          Python 3.X only, arguments that MUST be passed by keyword only in calls
    funct(*, name=value)  Function          Python 3.X only, arguments that MUST be passed by keyword only in calls

In a function call, using *iterable or **dict in a call alows us to package up arbitrarily many positional or keyword objects in sequences
(and other iterables) and dictionaries, respectively, and unpack them as separate, individual arguments when they are passed to the function.

In a function header, the *name form collects any extra unmatched positional arguments in a tuple, and the **name form collects extra keyword
arguments in a dictionary

In Python 3.X, any normal or defaulted argument named following a *name or a bare * are keyword-only arguments and must be assed by keyword in
calls.
'''

#Ejemplo

def testfunction(*pargs, **kargs):      #Accept arbitrary arguments
    print ('Called', pargs, kargs)      #Print the passed arguments

pargs1 = [1,2,3,4,5]
pargs2 = (6,7,8,9)
kargs1 = {'Juan': 1, 'Belon': 'MaxiGay'}
kargs2 = {'Alvarez':'Genius', 'Luis':'Charismatic'}


testfunction(pargs1,pargs2,kargs1,kargs2)
testfunction(1,2,3,4,5,7,Juan='Guapo',Belon='Feo')
