"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""
from fractions import Fraction
import math

gcds = {}

def gcd_recursive(a, b):
    global gcds
    
    if a == 1 or b == 1:
        return 1

    try:
        gcd = gcds[(a,b)]
        print('Found', a,b)
        return gcd
    except KeyError:
        pass

    gcd = math.gcd(a, b)
    gcds[(a,b)] = gcd
    
    return gcd

def get_hcf(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y

    hcf = 0
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i

    return hcf

def farey_sequence(n):
    answer, c = 2, 5
    b, d = 3, 7

    while c+d <= n:
        answer += b
        c += d

    return answer
 
def brute_force(limit):
    list = []
    for d in range(limit):
        if d % 1000 == 0:
            print ('processing', d)
        for n in range(d):
            gcd = math.gcd(n,d)
            if gcd  == 1:#gcd(n,d) == 1:
                list.append(n*1.0/d)
    
    list = sorted(list)
    for i in range(len(list)):
        if list[i] == 3.0/7:
            return Fraction(list[i-1]).limit_denominator().numerator
    return -1

def execute(n):
    result = farey_sequence(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(1000000)


