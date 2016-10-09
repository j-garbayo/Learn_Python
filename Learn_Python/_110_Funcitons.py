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