#coding: utf-8
#HIGHLIGHT - utf-8 coding
from _162_OOP_Chapter28_Basics_Example import Person

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

                IT ONLY CONTAINS INSTANCE ATTRIBTES, NOT CLASS ATRIBUTES!
        
                Because it is a dictionary, we can fetch its keys list, index by key,
                iterate over its keys, and so on, to process al attributes generically.
                We can use this here to print every attribyte in any instance, not just those
                we hardcode in custom displays.

'''

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    '''
    To minimize the chances of name collisions, Python programmers often prefix
    methods not meant for external use with a single underscore: _gatherAttrs in our case.
    This isn�t foolproof (what if another class defines _gatherAttrs, too?), but it�s usually
    sufficient, and it�s a common Python naming convention for methods internal to a class.
    '''
    def __gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self,key)))
        return ', '.join(attrs)
     
    def __repr__(self):
            return '[%s: %s]' % (self.__class__.__name__, self.__gatherAttrs())

if __name__ == '__main__':
    
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        def gatherAttrs(self):
            return 'Spam'

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()     # Make two instances
    print(X)                        # Show all instance attributes
    print(Y)                        # Show lowest class name

    #HIHLIGHT - HOW TO LIST INHERITED ATTRIBUTES IN CLASSES VIA dir()

    bob = Person('Bob Smith')

    #Instance attributes
    print 'bob.__dict__.keys: ', bob.__dict__.keys()

    #Instance an class iherited attributes and methods
    print 'dir(bob) :', dir(bob)