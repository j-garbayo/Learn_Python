#coding: utf-8

'''
HIGHLIGHT
- composites - nesting objects inside each other to build up composites (chapter 31)
we could use this composition idea to code our Manager extension by embedding a Person, 
instead of inheriting from it.

This pattern works in our example, but it requires about twice as much code and is less
well suited than inheritance to the kinds of direct customizations we meant to express
(in fact, no reasonable Python programmer would code this example this way in prac-
tice, except perhaps those writing general tutorials!)

Still, object embedding, and design patterns based upon it, can be a very good fit when
embedded objects require more limited interaction with the container than direct cus-
tomization implies.
    A controller layer, or proxy, like this alternative Manager, for ex-
    ample, might come in handy if we want to adapt a class to an expected interface it does
    not support, or trace or validate calls to another object�s methods (indeed, we will use
    a nearly identical coding pattern when we study class decorators later in the book)
'''

'''
HIGHLIGHT
__getattr__
Python also exports the list of all loaded
modules as the sys.modules dictionary and provides a built-in called getattr that lets
us fetch attributes from their string names�it�s like saying object.attr, but attr is an
expression that yields a string at runtime. Because of that, all the following expressions
reach the same attribute and object:

    M.name # Qualify object by attribute
    M.__dict__['name'] # Index namespace dictionary manually
    sys.modules['M'].name # Index loaded-modules table manually
    getattr(M, 'name') # Call built-in fetch function
'''

class Person:

    def __init__(self, name, job="None", pay=0): # Constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job # self is the new instance object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1] # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # Must change here only

    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print

class Manager:

    #HIGHLIGHT - Object embedding
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # Intercept and delegate

    #HIGHLIGHT - __getattr__ used for object method delegation
    def __getattr__(self, attr):
        y = getattr(self.person, attr)
        print('y = ', y)
        return getattr(self.person, attr) # Delegate all other attrs
        '''
        HIGHLIGHT
        what this does is allowing the user to use the methods in the embedded person object
        with the syntax manager.method instead of manager.person.method.
        '''
        '''
        __getattr__ explanation (from pytho documentation)
        CLASS INSTANCES
        A class instance is created by calling a class object (see above). 
        A class instance has a namespace implemented as a dictionary which is 
        the first place in which attribute references are searched. When an attribute 
        is not found there, and the instance’s class has an attribute by that name, the 
        search continues with the class attributes. If a class attribute is found that is 
        a user-defined function object or an unbound user-defined method object whose associated 
        class is the class (call it C) of the instance for which the attribute reference was 
        initiated or one of its bases, it is transformed into a bound user-defined method object 
        whose im_class attribute is C and whose im_self attribute is the instance. Static method 
        and class method objects are also transformed, as if they had been retrieved from class C; 
        see above under “Classes”. See section Implementing Descriptors for another way in which 
        attributes of a class retrieved via its instances may differ from the objects actually stored 
        in the class’s __dict__. 

        ***
        If no class attribute is found, and the object’s class has a __getattr__() method, that is 
        called to satisfy the lookup.
        ***

        Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary. 
        If the class has a __setattr__() or __delattr__() method, this is called instead of updating the 
        instance dictionary directly.

        Special attributes: __dict__ is the attribute dictionary; __class__ is the instance’s class.
        '''

    def __repr__(self):
        return str(self.person) # Must overload again (in 3.X)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000) # Make a Manager: __init__
    tom.giveRaise(.10) # Runs custom version
    print(tom.lastName()) # Runs delegated method
    print(tom) # Runs inherited __repr__
    print('--All three--')
    bob.giveRaise(0.2)