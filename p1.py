"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

target = 0

def brute_force(n):
    # return sum of all multiples of 3 and 4 below n
    result = 0

    for i in range(3,n):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i

    return result

def sum_divisible_by(m, target):
    # calculating the sum by formulae
    p = target // m
    rs = m * (p * (p + 1)) // 2
    return rs

def sum_multiples(n):
    n = n - 1 # since it has to be less than n
    return sum_divisible_by(3,n) + sum_divisible_by(5,n) - sum_divisible_by(15,n)

def execute(n):
    result = sum_multiples(n)
    print ("input: %i output: %i" %(n, result))
    
if __name__ == '__main__':
    execute(10)
    execute(1000)
