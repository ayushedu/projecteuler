"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def brute_force(n):
    # return product of pythagorean triplet whose sum is equal to n

    a,b,c = 0,0,0

    # start with n and get 3 numbers from it.
    a = 1

    while a < n:
        for b in range(a + 1, n-1):
            c = math.sqrt(a*a + b*b)
            # check if the are pythagoream triplet.
            if a + b + c == n:
                # return the product
                return a*b*c

        a += 1

    return -1

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(1000)
    


