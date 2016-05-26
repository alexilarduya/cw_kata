#http://www.codewars.com/kata/53ffbba24e9e1408ee0008fd

def knapsack(capacity, items):
    # Be greedy!
    v_to_s = [ item[1]/item[0] for item in items ]
    qty = [0] * len(items)
    
    while capacity > 0:
        max_v_to_s = 0
        index = None
        for idx, item in enumerate(items):
            if item[0] <= capacity:
                if max_v_to_s < v_to_s[idx]:
                    index = idx
                    max_v_to_s = v_to_s[idx]
        if index != None:
            qty[index] += 1
            capacity -= items[index][0]
        else:
            break
    return qty