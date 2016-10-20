import math

def is_prime(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def my_test(a):
    a.append(5)

print(is_prime(6))

a = [1,2]
my_test(a)
print(a)

#HIGHLIGHT - Functions as Objects
def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))

#HIGHLIGHT - Functions as arguments of other functions
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))