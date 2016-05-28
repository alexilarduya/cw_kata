#http://www.codewars.com/kata/541af676b589989aed0009e7/train/python


"""
Brute force approach, takes too long to compute but it is useful
to check results by myself
"""

import itertools

def count_change_brute(money, coins):

    coins = sorted(set(coins)) + [0]
    max_l = money // coins[0]
    combs = 0

    for option in itertools.combinations_with_replacement(coins ,max_l):
        if sum(option) == money:
            combs += 1

    return combs

# Implemented solution

def next_layer( coins, parent, money ):

    parent_ = []
    money_ = []
    comb = 0

    for father, m in zip(parent, money):
        for idx, coin in enumerate(coins[father:]):
            if m - coin > 0:
                parent_.append(father + idx)
                money_.append(m-coin)
            elif m - coin == 0:
                comb += 1

    return ( parent_, money_, comb )


def count_change(money, coins):

    combs = 0
    coins = sorted(set(coins))
    parent = [0]
    money = [money]

    while True:

        parent, money, n = next_layer( coins, parent, money )
        combs += n

        if len(money) == 0:
            break

    return combs

# Clever solution

def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])


        
        




















