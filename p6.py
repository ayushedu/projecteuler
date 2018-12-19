"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def brute_force(n):
    s1 = 0
    s2 = 0

    for i in range(1,n+1):
        s1 += i * i
        s2 += i


    s2 = s2 * s2
    return s2 - s1

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(100)
    


