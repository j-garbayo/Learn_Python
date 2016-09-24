import math
import collections
import string

def vol(rad):
    return (4/3)*math.acos(-1)*(rad**3) 

def check_presence(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False

def check_presence_alt(num, low, high):
    if num in range(low, high+1):
        return True
    else:
        return False

def up_low(s):
    n_low = 0
    n_up = 0

    for letter in s:
        if s.islower:
            n_low+=1
        elif s.isupper:
            n_up+=1

    print('n_low = ', n_low)
    print('n_up = ', n_up)
    
print(check_presence_alt(4.5,3,5))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

Sample_List = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_elements(lst):
    return list(set(lst))

print(unique_elements(Sample_List))

def multiply(numbers):
    a = 1
    for number in numbers:
        a *= number
    return a

print multiply([1,2,3,-4])

def palindrome(s):
    s = s.replace(" ","")
    if s == s[::-1]:
        return True

print(palindrome("madam"))
print(palindrome("nurses run"))

s = "pedo"
print set(s)

def ispangram(s, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    s = s.replace(" ","")
    s = set(s.lower())
    return alphaset <= s

s = "The quick brown fox jumps over the lazy dog"

print(ispangram(s))