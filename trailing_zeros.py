
"""
Write a program that will calculate the number of trailing zeros 
in a factorial of a given number.

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)

Be careful 1000! has length of 2568 digital numbers.

"""

def zeros(n):
    n_zeros = 0
    den = 5
    while n > den:
        n_zeros += int(n/den)
        den *= 5
    return n_zeros
        

# Added to initial solution

def zeros(n):
    x = n/5
    return x+zeros(x) if x else 0