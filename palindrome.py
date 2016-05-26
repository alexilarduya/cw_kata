#http://www.codewars.com/kata/556f4a5baa4ea7afa1000046/train/python

import itertools
from numpy import prod, zeros

def numeric_palindrome(*args):

    palindrome = 0
    
    for r in range(2,len(args)+1):
        combs = itertools.combinations(args, r)
        for option in combs:
            result = 1
            for n in option:
                result *= n
            if result != 0:
                tmp = max_pal(str(result))
                if int(tmp) > palindrome:
                    palindrome = int(tmp)

    return palindrome


def max_pal(strnum):
    char_list = [ int(char) for char in strnum]

    flag = False

    c_vect = zeros((10,2)).astype(int)
    biggest_odd = None

    for idx, _ in enumerate(c_vect):
        c_vect[idx,0] = char_list.count(idx)
        c_vect[idx,1] = c_vect[idx,0] // 2
        if c_vect[idx,0] %  2 == 1 and idx != 0:
            biggest_odd = idx

    if (c_vect[1:,1] == zeros(9)).all():
        c_vect[0,1] = 0

    if biggest_odd == None and c_vect[0,0] % 2 == 1:
        biggest_odd = 0

    res = ''

    for idx, _ in enumerate(c_vect):
        for _ in range(c_vect[idx,1]):
            res += str(idx)

    if isinstance(biggest_odd, int):
        return (res[::-1] + str(biggest_odd) + res)
    else:
        return(res[::-1] + res)