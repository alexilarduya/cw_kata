#http://www.codewars.com/kata/529bf0e9bdf7657179000008

from numpy import array

def min_square(board, num):
    
    i = num % 3
    j = num // 3
    
    return list(board[3*i : 3*(i+1), 3*j : 3*(j+1)].flatten())


def validSolution(board):

    valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    board = array(board)
        
    for i in range( board.shape[0] ):
        if not sorted(list(board[i,:])) == valid or \
           not sorted(list(board[:,i])) == valid or \
           not sorted(min_square(board, i)) == valid:
            return False
    
    return True