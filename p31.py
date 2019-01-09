"""
In England the currency is made up of pound, E, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can E2 be made using any number of coins?
"""

def count(S, m, n):
    print 'S', S, 'm', m, 'n', n
    # if n is zero there is only one solution - do not include any coin.
    if n == 0:
        return 1

    # if n is less than zero then no solution exist.
    if n < 0:
        return 0

    # if there are no coins and n is greater than 0, then no solution exist.
    if m <= 0 and n > 0:
        return 0

    return count(S, m - 1, n) + count(S, m, n - S[m-1])
    
def brute_force(S, n):
    return count(S, len(S), n)
    
def execute(S, n):
    result = brute_force(S, n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute([1,2,5,10,20,50,100,200], 200)

