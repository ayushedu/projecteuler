"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

primes = [2]
def is_prime(n):
    global primes

    for prime in primes:
        if n != prime and n % prime == 0:
            return False

    for i in range(primes[-1]+1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    primes.append(n)
    return True

def brute_force(n):
    count = 1
    i = 3
    last_prime = 2
    while count < n:
        if is_prime(i):

            count += 1
            last_prime = i

        i += 2

    return last_prime

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(1)
    execute(10001)
    


