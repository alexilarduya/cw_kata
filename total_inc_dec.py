#http://www.codewars.com/kata/total-increasing-or-decreasing-numbers-up-to-a-power-of-10/python

from numpy import zeros, array

sums = array([1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

def level(l):

    v = zeros(10).astype(int)
    v[-1] = 1
    v[-2] = 1

    while l > 0:
        l -= 1
        for j in range(10):
            v[j] = v[j]+v[j+1:].sum()

    return v.dot(sums)


def total_inc_dec(x):
    if x == 0:
        return 1
    if x == 1:
        return 10
    if x > 1:
        return = level(x-2) - 10 + total_inc_dec(x-1)