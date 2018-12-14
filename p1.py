"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(n):
    # return sum of all multiples of 3 and 4 below n
    result = 0

    for i in range(3,n):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i

    return result

def execute(n):
    result = sum_multiples(n)
    print ("input: %i output: %i" %(n, result))
    

if __name__ == '__main__':
    execute(10)
    execute(1000)
