"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math

primes = [2]

def is_prime(n):
    # return if n is prime
    for prime in primes:
        if n == prime:
            return True
        elif n % prime == 0:
            return False

    for i in range(primes[-1] + 1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    primes.append(n)
    return True

def brute_force(n):
    # return sum of all primes below n
    sum = 2
    for i in range(3,n, 2):
        if i % 10001 == 0:
            print 'processing', i
        if is_prime(i):
            sum += i
              
    return sum

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(2000000)
    


