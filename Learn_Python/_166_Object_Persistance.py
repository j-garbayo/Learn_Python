from _165_OOP_person import Person, Manager
import shelve
import glob

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

    db = shelve.open('C:\Users\Juan\persondb')
    for obj in (bob, sue, tom):
        db[obj.name] = obj
    db.close()
    '''
    With Python 3.X and no extra software
    installed, our database is stored in three files (in 2.X, it�s just one file, persondb, because
    the bsddb extension module is preinstalled with Python for shelves; in 3.X, bsddb is an
    optional third-party open source add-on).
    '''

    print(glob.glob('person*'))


    print('end')

'''
Notice that we don�t have to import our Person or Manager classes here in order to load
or use our stored objects. For example, we can call bob�s lastName method freely, and
get his custom print display format automatically, even though we don�t have his
Person class in our scope here. This works because when Python pickles a class instance,
it records its self instance attributes, along with the name of the class it was created
from and the module where the class lives. When bob is later fetched from the shelve
and unpickled, Python will automatically reimport the class and link bob to it.
The upshot of this scheme is that class instances automatically acquire all their class
behavior when they are loaded in the future. We have to import our classes only to
make new instances, not to process existing ones. Although a deliberate feature, this
scheme has somewhat mixed consequences:

� The downside is that classes and their module�s files must be importable when an
instance is later loaded. More formally, pickleable classes must be coded at the top
level of a module file accessible from a directory listed on the sys.path module
search path (and shouldn�t live in the topmost script files� module __main__ unless 
they�re always in that module when used). Because of this external module file
requirement, some applications choose to pickle simpler objects such as diction-
aries or lists, especially if they are to be transferred across the Internet.

� The upside is that changes in a class�s source code file are automatically picked up
when instances of the class are loaded again; there is often no need to update stored
objects themselves, since updating their class�s code changes their behavior.
'''

'''
For another example of object persistence in this book, see the sidebar in Chapter 31
titled �Why You Will Care: Classes and Persistence� on page 941. It stores a some-
what larger composite object in a flat file with pickle instead of shelve, but the effect
is similar. For more details and examples for both pickles and shelves, see also Chap-
ter 9 (file basics) and Chapter 37 (3.X string tool changes), other books, and Python�s 
manuals.
'''