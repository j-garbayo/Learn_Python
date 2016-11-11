'''
###Problem 1
Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
The function will have an input of a string, and output a list of integers.
'''

def word_lengths(phrase):
    return map(len,phrase.split(" "))

print(word_lengths('How long are the words in this phrase'))

'''
###Problem 2
Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!
'''

def digits_to_num(digits):
    return reduce(lambda x,y: 10*x + y, digits)

print(digits_to_num([3,4,3,2,1]))

'''
###Problem 3
Use filter to return the words from a list of words which start with a target string.
'''

def filter_words(word_list, expression):
    return filter(lambda word: word[0:len(expression)]==expression, word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print filter_words(l, 'h')

'''
###Problem 4
Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated 
together with connector between them. Look at the example output below:
'''

def concatenate(L1, L2, conector):
    return [t[0] + conector + t[1] for t in zip(L1,L2)]

print(concatenate(['A','B'],['a','b'],'-'))

#ALTERNATIVE SYNTAX FOR THE LIST COMPREHENSION

def concatenate_2(L1,L2, conector):
    return [word1 + conector + word2 for (word1, word2) in zip(L1,L2)]

print(concatenate_2(['A','B'],['a','b'],'-'))

'''
###Problem 5
Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. 
You may assume that a value will only appear once in the given list.
'''

#NOTE: Dictionary comprehensions (similar to list comprehensions) are necessary here. See 'Advanced Dictionaries'
def d_list(L):
    return {item:number for number, item in enumerate(L)}


lst = ['a','b','c']
print((d_list(lst)))

'''
###Problem 6
Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.
'''

def count_match_index(L):
    return len(filter(lambda t: t[0]==t[1],list(enumerate(L))))
    #EXPLANATION
        # - list(enumerate(L)) returns a list of tuples in the form [(count_1, item_1), ...]
        # - The lambda expression given as an argument for 'filter' uses these tuples as argument
        # - len() is applied to the list

print(count_match_index([0,2,2,1,5,5,6,10]))

#ALTERNATIVE! Introduce an "if" condition in the list comprehension

def count_match_index_2(L):
    return len([num for count, num in enumerate(L) if num == count])

print(count_match_index_2([0,2,2,1,5,5,6,10]))