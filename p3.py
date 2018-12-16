"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
primes = [2]

def is_prime(n):
    global primes
    last_prime = 2

    for prime in primes:
        if n % prime == 0:
            return False
        last_prime = prime

    # check if number is prime
    for i in range(last_prime, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    primes.append(n)
    return True

def brute_force(n):
    # return largest prime of n

    factors = []
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
        
    largest_prime = -1
    for factor in factors:
        if is_prime(factor) and largest_prime < factor:
            largest_prime = factor

    return largest_prime


def execute(n):
    result = brute_force(n)
    print ("input, result", n, result)
    
if __name__ == '__main__':
    execute(13195)
    execute(600851475143)


