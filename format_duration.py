#http://www.codewars.com/kata/human-readable-duration-format/

from numpy import zeros

def format_duration(seconds):

    if seconds == 0:
        return 'now'
    
    str_list = []
    keys     = ['year', 'day', 'hour', 'minute', 'second']
    secs_key = [ 365 * 24 * 60 * 60, 24 * 60 * 60, 60*60, 60, 1]
    
    for k, t in zip(keys, secs_key):    
        if seconds // t > 1:
            str_list.append(str(seconds//t) + ' ' + k + 's')
        elif seconds // t == 1:
            str_list.append('1 ' + k)
        seconds = seconds % t
        
    if len(str_list) > 1:
        return ', '.join(str_list[:-1]) + ' and ' + str_list[-1]
    else:
        return str_list[0]