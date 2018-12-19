"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def brute_force(n):
    # return hcf of numbers from 1 to n
    rs = 2

    for i in range(3, n+1):
        if rs % i == 0: # n is divisible by i - do nothing
            continue
        
        rem = rs % i 
        if i % rem == 0:  
            rs = rs * (i // rem)
        else:
            rs *= i


    return rs


def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(20)
    


