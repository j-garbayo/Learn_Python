import math

# Create a new object type called Sample
class Sample(object):
    pass

# Instance of Sample
x = Sample()

print type(x)

#ATTRIBUTES
'''
An **attribute** is a characteristic of an object.
A **method** is an operation we can perform with the object.
'''

#Initialzing attributes
##Attributes
'''
The syntax for creating an attribute is:
    
    self.attribute = something
    
There is a special method called:

    __init__()

This method is used to initialize the attributes of an object. For example:
'''

class Dog(object):
    def __init__(self,breed):
        #Each attribute in a class definition begins with a reference to the instance object. 
        #It is by convention named self. The breed is the argument. The value is passed during the class instantiation.
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print sam.breed
print frank.breed

#Class Object Atributes
'''
They are the same for any instance of the class
'''

class Dog2(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog2("Lab","Sam")

print sam.species

#METHODS
'''
Functions defined inside the body of the class, used to perform operations
with the attributes of our objects. Essential for encapsulation.
Essentially: methods are functions acting on an object that take the object
itself into account trhough it "self" argument.
'''

class Circle(object):

    pi = math.acos(-1)

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius**2*Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius


c = Circle()

c.setRadius(2)
print 'Radius is: ',c.getRadius()
print 'Area is: ',c.area()
    
class Animal(object):
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog3(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "Woof!"

d = Dog3()

d.whoAmI()
d.eat()
d.bark()

#SPECIAL METHODS
'''
From book "Learning Python"
Operator overloading
By providing special protocol methods, classes can define objects that respond to
the sorts of operations we saw at work on built-in types. For instance, objects made
with classes can be sliced, concatenated, indexed, and so on. Python provides
hooks that classes can use to intercept and implement any built-in type operation.
'''


class Book(object):
    #FOR A COMPLETE LIST OF SPECIAL METHODS, SEE PYTHOn DOCUMENTATION, LINK ON ONE-NOTE.

    def __init__(self, title, author, pages):
        #Called after the instance has been created (by __new__()), 
        #but before it is returned to the caller. The arguments are those passed to the class constructor expression.
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        #Called by the str() built-in function and by the print statement to compute the “informal” string representation of an object. 
        #This differs from __repr__() in that it does not have to be a valid Python expression: a more convenient or concise representation 
        #may be used instead. The return value must be a string object.
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        #Called to implement the built-in function len(). Should return the length of the object, an integer >= 0. 
        #Also, an object that doesn’t define a __nonzero__() method and whose __len__() method returns zero is considered 
        #to be false in a Boolean context.
        return self.pages

    def __del__(self):
        #run automatically when an instance's space is being reclaimed(i.e., at “garbage collection” time):
        #it can also be explicitly called
        print "A book is destroyed"

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print book
s = str(book)
print ("str: " + s)
print len(book)
del book
