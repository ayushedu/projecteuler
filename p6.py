"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def get_diff(n):
    sum = n * (n+1) // 2 # sum of first n natural numbers
    sum_sq = (2*n+1) * (n+1) * (n) // 6 # sum of squares of first n natural numbers
    
    return (sum * sum) - sum_sq

def brute_force(n):
    s1 = 0
    s2 = 0

    for i in range(1,n+1):
        s1 += i * i
        s2 += i


    s2 = s2 * s2
    return s2 - s1

def execute(n):
    result = get_diff(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(100)
    


