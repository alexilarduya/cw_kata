def iq_test(numbers):
    odd, even = [], []
    for idx, n in enumerate(numbers.split(' ')):
        if int(n) % 2 == 0:
            even.append(idx+1)
        else:
            odd.append(idx+1)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]
