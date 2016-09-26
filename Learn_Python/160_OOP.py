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

