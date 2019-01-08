"""
How many routes are there through a 20x20 grid?
"""

def traverse(i, j, n):
    #print 'Traversing %i x %i' %(i, j)
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
    result = brute_force(n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(20)
    #print get_chain(13)
    


# 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# 12 6 3 10 5 16 8 4 2 1
# 4 2 1: 3
# 3 10 5 16 8 4 2 1: 8
# 1 2  3 4  5 6 7 8 
