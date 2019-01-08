"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

amiables = set()
def get_amiable(n):
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i

    return sum

def find_amiable(n):
    global amiables
    
    if n in amiables:
        return

    n1 = get_amiable(n)
    n2 = get_amiable(n1)

    if n == n1 and n == n2:
        return 

    if n == n2:
        amiables.add(n)
        amiables.add(n1)

def brute_force(n):
    for i in range(2,n):
        if i % 100 == 0:
            print 'processing', i
        find_amiable(i)

    global amiables
    return sum(amiables)
    
def execute(n):
    result = brute_force(n)
    global amiables
    print amiables
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(10000)

