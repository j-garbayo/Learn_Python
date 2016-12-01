'''
Regular expressions are text matching patterns described with a formal syntax. You'll often hear regular expressions referred
to as 'regex' or 'regexp' in conversation. Regular expressions can include a variety of rules, for finding repetition, text-matching,
and much more. AS you advance in Python you'll see that a lot of your parsing problems can be solved with regular expressions.

They are also a common interview question!

If you are familiar with Perl, you'll notice that the syntax for regular expressions are very similar in Python. We will be using
the 're' module with Python for this lexture.

Let us get started!
'''

#RE.SEARCH
#ill take the pattern, scan the text, and then returns a Match object. If no pattern is found, 
#a None is returned. To give a clearer picture of this match object, check out the cell below:

import re 

#List of patterns to search for:
patterns = ['term1', 'term2']

#Text to parse:
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print 'Searching for "%s" in: \n "%s"' % (pattern, text)
    
    #Check for match
    if re.search(pattern, text):
        print '\n'
        print 'Match was found. \n'
    else:
        print '\n'
        print 'No match was found. \n'

#Examining the match object
pattern = 'term1'

#Text to parse
text = 'This is a string with term1, twice term1, but it does not have the other term.'
    
match = re.search(pattern, text)

print(type(match))

#Show start and end of match
print(match.start())
print(match.end())

#SPLIT WITH REGULAR EXPRESSIONS
split_term = '@'

phrase = 'What is the domain name of someone with the e-maio: help@gmail.com'

#split the phrase
print(re.split(split_term,phrase))
print(phrase.split('@'))

#FINDING ALL INSTANCES:

#Examining the match object
pattern = 'term1'

#Text to parse
text = 'This is a string with term1, twice term1, but it does not have the other term.'

matches = re.findall(pattern, text)

type(matches)
print(matches)

