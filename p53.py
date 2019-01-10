"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.
How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
"""

factorials = {}

def get_factorial(n):
    global factorials

    try:
        factorials[n]
    except KeyError:
        pass
       

    if n <= 1:
        return 1

    factorial = n * get_factorial(n-1)
    factorials[n] = factorial
    return factorial
        

def get_combination(n):
    count = 0
    for r in range(2,n):
        if get_factorial(n) / (get_factorial(r) * get_factorial(n-r)) > 1000000:
            count += 1
    
    return count

def brute_force(limit):
    count = 0
    for n in range(2, limit+1):
        count += get_combination(n)

    return count

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(100)


