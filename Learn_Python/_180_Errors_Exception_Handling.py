'''
try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 
'''

try:
    #f = open('testfile','w')    #provides write permission
    f = open('testfile','r')    #does not provide write permission
    f.write('Test write this')
#except IOError:     #checks only for IOErrors
except:
    # This will only check for an IOError exception and then execute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written successfully"
   f.close()

'''
What if we kept wanting to run code after the exception occurred?
FINALLY
'''

'''
The finally block will always run, regardless of whether an exception occurs or not.

try:
   Code block here
   ...
   Due to any exception, this code may be skipped!
finally:
   This code block would always be executed.

'''

#def askint():
#        #This version does not ensure that "val" is properly assigned and might yield an error
#        try:
#            val = int(raw_input("Please enter an integer: "))
#        except:
#            print "Looks like you did not enter an integer!"
            
#        finally:
#            print "Finally, I executed!"
#        print val   

def askint():
    while True:
        #HIGHLIGHT: yet another way of checking for integers.
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you did not enter an integer!"
            continue
        else:
            print 'Yep thats an integer!'
            break
        finally:
            print "Finally, I executed!"
    print val 

askint()

#HIGHTLIGHT - Raising Exceptions
'''
Exceptions can be raised with arguments that give detail about them.
For example:
'''

name = "123"
raise NameError("Invalid name!")

'''
In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
'''
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise

#HIGHLIGHT - Assertions

'''
An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.

Programmers often place assertions at the start of a function to check for valid input, 
and after a function call to check for valid output.
'''

temp = -10
assert (temp >= 0), "Colder than absolute zero!"