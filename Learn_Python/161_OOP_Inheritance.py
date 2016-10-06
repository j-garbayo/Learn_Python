
#HIGHLIGHT: CLASS OBJECT atributes (a.k.a Data attributes), shared by all instances
#e.g. Tracking the number of instances of a certain object.
class SharedData(object):

        spam = 42

x = SharedData()
y = SharedData()

print x.spam, y.spam

SharedData.spam = 50

print x.spam, y.spam

x.spam = 60

print x.spam, y.spam


#HIGHLIGHT: Class object attributes and object (shared class data) vs Instance attributes (per-instance data)
class MixedNames: # Define class

     data = 'spam' # Assign class attr
     def __init__(self, value): # Assign method name
        self.data = value # Assign instance attr
     def display(self):
        print(self.data, MixedNames.data) # Instance attr, class attr

x = MixedNames(1)
y = MixedNames(2)

x.display(); y.display()

'''
HIGHLIGHT - CLASS VS INSTANCE ATTRIBUTES WITH AN EXAMPLE (view foregoing example)
The net result is that data lives in two places: in the instance objects (created by the
self.data assignment in __init__), and in the class from which they inherit names
(created by the data assignment in the class). The class�s display method prints both
versions, by first qualifying the self instance, and then the class.
'''

#EXAMPLE OF METHOD CALLING BY CLASS INSTEAD OF BY INSTANCE
class NextClass: # Define class

     def printer(self, text): # Define method
         self.message = text # Change instance
         print(self.message) # Access instance

x = NextClass()
x.printer('instance call')
print x.message
NextClass.printer(x, 'class call')
print x.message

'''
HIGHLIGHT - METHOD EXTENSION BY INHERITANCE
Direct superclass method calls are the crux of the matter here. The Sub class replaces
Super�s method function with its own specialized version, but within the replacement,
Sub calls back to the version exported by Super to carry out the default behavior. In
other words, Sub.method just extends Super.method�s behavior, rather than replacing it
completely:
'''

class Super():
     def method(self):
        print('in Super.method')

class Sub(Super):
     def method(self): # Override method
         print('starting Sub.method') # Add actions here
         Super.method(self) # Run default action
         print('ending Sub.method')

x = Super()
x.method()

x = Sub()
x.method()
