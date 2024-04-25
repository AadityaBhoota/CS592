def geometric_sum(n):
    if n <= 0:
        return 0
    
    geometric_sum = 0
    for i in range(n):
        geometric_sum += 1 / (2**i)
    
    return geometric_sum

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)