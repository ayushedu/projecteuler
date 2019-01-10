"""
It can be seen that n=6 produces a maximum n/theta(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/theta(n) is a maximum.
"""

def get_relative_prime(n):
    rprimes = [1]

    for i in range(2, n):
        rprimes.append(i)

    for p in rprimes[1:]:
        if n % p == 0:
            while p < n:
                rprimes[p-1] = None
                p += p

    rprimes = [v for v in rprimes if v]
    return len(rprimes)

def brute_force(limit):
    ratio = 0
    val = 0
    for n in range(2,limit):
        if n % 1000 == 0:
            print 'Processing', n
        tmp_ratio = n / get_relative_prime(n)
        if tmp_ratio > ratio:
            ratio = tmp_ratio
            val = n

    return val

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
   
if __name__ == '__main__':
    execute(1000000)


