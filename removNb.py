# https://www.codewars.com/kata/is-my-friend-cheating

def removNb(n):

    res_list = []

    sum_seq = n * (n+1) / 2
    min_lim = sum_seq - 2 * n

    for i in range( n+1, int(sqrt(min_lim)), -1):

        j = int(min_lim / i) 

        while j < i:

            j+= 1
            if j * i == sum_seq - j - i:
                res_list.append((j,i))
            elif j * i > sum_seq -j - i:
                break
                
    for element in res_list[::-1]:
        res_list.append(element[::-1])

    return res_list



