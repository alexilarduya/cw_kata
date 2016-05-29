#http://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

from numpy import all, array, hstack, ones, vstack, zeros

def build_ship(sz):

    ship = ones(sz + 2)
    ship[0] = ship [-1] = 0

    return vstack([zeros(sz + 2), ship, zeros(sz + 2)])

def validateBattlefield(field):
    
    fld = zeros([12,12])
    fld[1:-1,1:-1] = array(field)
    tfld = fld.T

    for sz, n in zip([1,2,3,4], [8,3,2,1]):
        
        N = 0
        boat = build_ship(sz)

        for x in range(9):
            for y in range(10 - sz):

                if all( fld[ x:x+3, y:y+sz+2] == boat ):
                    N += 1
                if all( tfld[x:x+3, y:y+sz+2] == boat ):
                    N += 1

        if N != n:
            return False

    return True