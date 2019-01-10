"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(n):
    s = str(n)

    mid = len(s)//2
    i = 0
    
    while i < mid:
        if s[i] != s[-i-1]:
            return False

        i += 1

    return True
            
def get_binary(n):
    return "{0:b}".format(n)
   
    
def brute_force(max):
    list = []
    
    for i in range(max):
        binary = get_binary(i)
        if is_palindrome(i) and is_palindrome(binary):
            print 'Found', i, binary
            list.append(i)
    print list
    return sum(list)

def execute(n):
    result = brute_force(n)
    print ("Result: ", result)
    
   
if __name__ == '__main__':
    execute(1000000)


