# File person.py (start)

'''
HIGHLIGHT
Inheritance and composition
Interestingly, this code uses both inheritance and composition—Department is a com-
posite that embeds and controls other objects to aggregate, but the embedded Person
and Manager objects themselves use inheritance to customize. 

As another example, a
GUI might similarly use inheritance to customize the behavior or appearance of labels
and buttons, but also composition to build up larger packages of embedded widgets,
such as input forms, calculators, and text editors. The class structure to use depends
on the objects you are trying to model—in fact, the ability to model real-world entities
this way is one of OOP’s strengths.
'''

'''
HIGHLIGHT - Introspection methods
HIGHLIGHT - instance.__class__ 
                provides a link from an instance to the class from which it was created
HIGHLIGHT -     __name__ - gives the classes' name
HIGHLIGHT -     __bases__ - gives the classes' superclasses
                    Can be used to print the name of the class from which
                    an instance is made rather than one we've hardcoded.
HIGHLIGHT - object.__dict__ 
                provides a dictionary with one key/value pair for every attribute attached
                to a namespace object (including modules, clases and instances)
        
                Because it is a dictionary, we can fetch its keys list, index by key,
                iterate over its keys, and so on, to process al attributes generically.
                We can use this here to print every attribyte in any instance, not just those
                we hardcode in custom displays.

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

class Manager(Person):

    def __init__(self, name, pay): # Redefine constructor
        Person.__init__(self, name, 'mgr', pay) # Run original with 'mgr'

    def giveRaise(self, percent, bonus=.10):
        #HIGHLIGHT - CALLING BY CLASS TO EXTEND BEHAVIOUR
        Person.giveRaise(self, percent + bonus) # Good: augment original

#HIGHLIGHT!! Uses varargs (* or **) see chapter 18 or summary in one note
#
class Department:

    def __init__(self, *args):
        print 'printing list'
        print list(args)
        print 'exit printing list'
        #Converts the arguments to a list
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)    

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)    

'''
Although we could split the test code off into a separate file, it�s often more convenient
to code tests in the same file as the items to be tested. It would be better to arrange to
run the test statements at the bottom only when the file is run for testing, not when the
file is imported. That�s exactly what the module __name__ check is designed for, as you
learned in the preceding part of this book. Here�s what this addition looks like�add
the require test and indent your self-test code:
'''

'''
HIGHLIGHT
Aggregatuin if akk ibhects un irder to treat them as a set using object delegation

- Varargs collecting: collect arbitrarily many positional or keyword arguments
    Functions can use special arguments preceded with one or two * characters to
    collect an arbitrary number of possibly extra arguments. This feature is often re-
    ferred to as varargs, after a variable-length argument list tool in the C language; in
    Python, the arguments are collected in a normal object.

- Varargs unpacking: pass arbitrarily many positional or keyword arguments
    Callers can also use the * syntax to unpack argument collections into separate
    arguments. This is the inverse of a * in a function header—in the header it means
    collect arbitrarily many arguments, while in the call it means unpack arbitrarily
    many arguments, and pass them individually as discrete values.
'''

'''
HIGHLIGHT - Varargs * and **
'''

#HIGHLIGHT - Very Important Using main to indicate that the module shall only be run as a script

#if __name__ == '__main__':
#    bob = Person('Bob Smith')
#    sue = Person('Sue Jones', job='dev', pay=100000)
#    print(bob)
#    print(sue)
#    print(bob.lastName(), sue.lastName())
#    sue.giveRaise(.10)
#    print(sue)
#    tom = Manager('Tom Jones', 50000) # Make a Manager: __init__
#    tom.giveRaise(.10) # Runs custom version
#    print(tom.lastName()) # Runs inherited method
#    print(tom) # Runs inherited __repr__
#    print('--All three--')
#    bob.giveRaise(0.2)

#    #HIGHLIGHT - Python's polimorphsim with objects and inheritance
#    for obj in (bob, sue, tom): # process objects generically
#        obj.giveRaise(.10) # run this object's giveraise
#        print(obj) # run the common __repr__

'''
HIGHLIGHT - __str__ vs __repr__
as we�ll learn in Chapter 30, the __repr__ method is often used to provide
an as-code low-level display of an object when present, and __str__ is reserved for
user-friendly informational displays like ours here. Sometimes classes provide both
__str__ for user-friendly displays and a __repr__ with extra details for developers
view. Because printing runs __str__ and the interactive prompt echoes results
__repr__, this can provide both target audiences with an appropriate display.
'''

'''
Technically, bob and sue are both namespace objects�like all
class instances, they each have their own independent copy of the state information
created by the class. Because each instance of a class has its own set of self attributes,
classes are a natural for recording information for multiple objects this way; just like
built-in types such as lists and dictionaries, classes serve as a sort of object factory.
'''

'''
HIGHLIGHT - BASICS OF OOP
In this complete form, and despite their relatively small sizes, our classes capture nearly
all the important concepts in Python’s OOP machinery:
• Instance creation—filling out instance attributes
• Behavior methods—encapsulating logic in a class’s methods
• Operator overloading—providing behavior for built-in operations like printing
• Customizing behavior—redefining methods in subclasses to specialize them
• Customizing constructors—adding initialization logic to superclass steps

based upon just three simple ideas: 
• the inheritance search for attributes in object trees
• the special self argument in methods
• operator overloading’s automatic dispatch to methods.

advanced class concepts (later chapters), such as 
- decorators.
- metaclasses.
- ccomposites - nesting objects inside each other to build up composites (chapter 31)
'''

if __name__ == "__main__":

        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job = 'dev', pay = 100000)
        tom = Manager('Tom Jones', 50000)

        #development = Department(bob, sue)   #Embed objects in a composite
        #development.addMember(tom)           
        #development.giveRaises(0.10)        # Runs embedded objects' giveRaise
        #development.showAll()               # Runs embedded objects' __repr__

        bobdict = bob.__dict__

        for k in bobdict:
            print k + "->" + str(getattr(bob, k))
            
        print bobdict
