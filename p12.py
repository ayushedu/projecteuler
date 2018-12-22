"""
What is the value of the first triangle number to have over five hundred divisors?
"""

factors = {}

def getFactors(n):
    global factors
    numFactors = 1

    # get number of factors
    for i in range(n, 1, -1):
        if n % i == 0:
            if factors.has_key(i):
                numFactors += factors[i]
                break
            else:
                numFactors += 1

    factors[n] = numFactors
        

def brute_force(n):
    counter = 1
    triangleNum = 1

    # generate triangle numbers
    while True:
        triangleNum = counter * (counter+1)//2
        numFactors = 1 # including 1 as the factor by default

        # check how many factors does it have
        for i in range(2,triangleNum+1):
            if triangleNum % i == 0:
                numFactors += 1

        if numFactors > n:
            return triangleNum
    

        counter += 1


    return -1
    
    

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(500)
    


