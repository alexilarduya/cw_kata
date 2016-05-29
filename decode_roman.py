#http://www.codewars.com/kata/51b6249c4612257ac0000005

chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [  1, 5, 10, 50, 100, 500, 1000]

r_dict = {}
for c, v in zip(chars, values):
    r_dict[c] = v


def solution(roman):

    total = 0
    acc = 0
    last_char = None

    for c in roman:

        if last_char == None or last_char == r_dict[c]:
            acc += r_dict[c]

        elif last_char > r_dict[c]:
            total += acc
            acc = r_dict[c]

        elif last_char < r_dict[c]:
            total -= acc
            acc = r_dict[c]

        last_char = r_dict[c]

    return total + acc