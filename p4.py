"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    # check if number is palindome

    s = str(n)
    lo = 0
    hi = len(s) - 1
    
    while lo <= hi:
        if s[lo] != s[hi]:
            return False

        lo += 1
        hi -= 1

    return True

def brute_force(start, end):
    palindrome = -1
    for i in range(end, start - 1, -1):
        for j in range(i, start - 1, -1):
            if is_palindrome(i*j) and i*j > palindrome:
                palindrome = i*j

    return palindrome


def execute(i, j):
    result = brute_force(i, j)
    print ("Palindrome", result)
    
if __name__ == '__main__':
    execute(100, 999)
    


