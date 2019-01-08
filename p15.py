"""
How many routes are there through a 20x20 grid?
"""

cache = {}
grid = []


def count_routes(m, n):

    grid = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(m + 1):
        grid[i][0] = 1

    for j in range(n + 1):
        grid[0][j] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[m][n]

    

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

