'''
__call__

the __call__ method is called when the instance is called (in the same manner as a function). Python runs a __call__ method for
function call expressions applied to the instances, passing along whatever positional or keyword arguments were sent. 

IMPORTANCE OF THE __call__ OPERATOR OVERLOADING METHOD
- It allows instances to conform to a function based APIs. I.e. APIs that expect functions
    - Allows us to code objects that conform to an expected function call interface, but also retain state information (properties)
      and other class assets such as inheritance. In fact, it may be the third most commonly used operator overloading method, behind 
      the __init__ constructor and the __str__ and __repr__ display-format alternatives 
'''

#Examples

class Callee:
    def __call__(self, *pargs, **kwargs):   #Intercept instance calls
        print('Called:', pargs, kwargs)     #Displays the arguments

C = Callee()    #Creates an instance
C(1,2,3)        #Calls the instance
C(1,2,3,x=4,y=5)

pargs = ('ahi','si','voy')
kwargs = {'con':'lo','que':'te','doy':':)'}

C(pargs,kwargs)