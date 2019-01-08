"""
How many routes are there through a 20x20 grid?
"""

cache = {}

def count_routes(m, n):
    global cache

    if n == 0 or m == 0:
        return 1

    if (m,n) in cache:
        return cache[(m,n)]

    count = count_routes(m, n - 1) + count_routes(m - 1, n)
    cache[(m,n)] = count
    return count

    

def traverse(i, j, n):
    print 'Traversing %i x %i' %(i, j)
    count = 0
    
    # traverse left
    if i < n:
        count += traverse(i + 1, j, n)

    # traverse right
    if j < n:
        count += traverse(i, j + 1, n)

    if i == n and j == n:
        return count + 1
    else:
        return count


def brute_force(n):
# return no of routes from 0,0 to n,n
    return traverse(0, 0, n)
        

    
def execute(n):
    #result = brute_force(n)
    result = count_routes(n,n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(20)

