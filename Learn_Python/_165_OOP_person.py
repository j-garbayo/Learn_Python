from _164_OOP_classtools import AttrDisplay

class Person(AttrDisplay):
    '''
    Create and process person records
    '''
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self): # Assumes last is last
        return self.name.split()[-1]
    def giveRaise(self, percent): # Percent must be 0..1
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay) # Job name is implied
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':

    '''
    When we run this code now, we see all the attributes of our objects, not just the ones
    we hardcoded in the original __repr__. And our final issue is resolved: because AttrDis
    play takes class names off the self instance directly, each object is shown with the name
    of its closest (lowest) class
    '''

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)