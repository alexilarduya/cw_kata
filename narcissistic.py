#http://www.codewars.com/kata/does-my-number-look-big-in-this
def narcissistic( value ):
    tmp = 0
    p = str(value)
    for c in p:
        tmp += int(c) ** len(p)
    if value == tmp:
        return True
    else:
        return False