#FROM CHAPTER 28 of the book LEARNING PYTHON


'''
To minimize the chances of name collisions like this, Python programmers often prefix
methods not meant for external use with a single underscore: _gatherAttrs in our case.
This isn�t foolproof (what if another class defines _gatherAttrs, too?), but it�s usually
sufficient, and it�s a common Python naming convention for methods internal to a class.
A better and less commonly used solution would be to use two underscores at the front
of the method name only: __gatherAttrs for us. Python automatically expands such
names to include the enclosing class�s name, which makes them truly que when
looked up by the inheritance search. This is a feature usually called pseudoprivate class
attributes, which we�ll expand on in Chapter 31 and deploy in an expanded version of
this class there. For now, we�ll make both our methods available.To minimize the chances of name 
collisions like this, Python programmers often prefix
methods not meant for external use with a single underscore: _gatherAttrs in our case.

This isn�t foolproof (what if another class defines _gatherAttrs, too?), but it�s usually
sufficient, and it�s a common Python naming convention for methods internal to a class.
A better and less commonly used solution would be to use two underscores at the front
of the method name only: __gatherAttrs for us. Python automatically expands such
names to include the enclosing class�s name, which makes them truly unique when
looked up by the inheritance search. This is a feature usually called pseudoprivate class
attributes, which we�ll expand on in Chapter 31 and deploy in an expanded version of
this class there. For now, we�ll make both our methods available.
'''