def geometric_sum(n):
    '''
    Calculate the geometric sum of n-1 terms.
    '''
    total_sum = 0
    for i in range(n-1):
        total_sum += 1/(2**i)
    return total_sum

# Testing the function




def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)