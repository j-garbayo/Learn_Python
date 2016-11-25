'''
Syntactically, generator expressions are just like normal list comprehensions, and 
support all their syntax, inclding 'if filters' and 'loop nesting'. Byt they are enclosed in parentheses
instead of square brackets (like tuples, their enclosing parentheses are often optional):
'''

#List comprehension: build a list
print([x ** 2 for x in range (4)])

#Generator expression: make an iterator
gen_expr = (x**2 for x in range(4))
print(gen_expr)

for i in range(4):
    print next(gen_expr)

#At least on a functionality basis, coding a list comprehension is essentially the same
#as wrapping a generator expression in a 'list' built-in call to force it to produce
#all its results in a list at once

'''
See the book Learn Python for a full review of Generator Expressions
'''
