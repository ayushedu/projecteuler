"""
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

series = {}

def get_chain(k):
    global series
    count = 1
    n = k
    while n > 1:
        if n in series:
            count += series[n] - 1 # preventing 1 from counted twice
            break

        if n % 2 == 0:
            n_tmp = n // 2
        else:
            n_tmp = 3 * n + 1

        count += 1
        n = n_tmp

    series[k] = count

    return count

def brute_force(n):
    count = -1

    for i in range(2, n + 1):
        if i % 100000 == 0:
            print '--> ', i

        tmp_count =  get_chain(i)

        if tmp_count > count:
            count = tmp_count

    return count

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(1000000)
    #print get_chain(13)
    


# 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# 12 6 3 10 5 16 8 4 2 1
# 4 2 1: 3
# 3 10 5 16 8 4 2 1: 8
# 1 2  3 4  5 6 7 8 
