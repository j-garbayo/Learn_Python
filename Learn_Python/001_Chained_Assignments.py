'''
In Python, chained assignments are possible, but are different
than in C. The following example illustrates how changed assignment
differs from normal assignment. Think of changed assignment in terms of
making two names reference the same object
'''

def createlist():
    return []

x = y = createlist()
print('x = ', x)
print('y = ', y)

x.append(4)
print('x = ', x)
print('y = ', y)

x = createlist(); y = createlist()  #Use only this kind of syntax (semicolon) if it improves readability
x.append(3)
y.append(4)
print('x = ', x)
print('y = ', y)