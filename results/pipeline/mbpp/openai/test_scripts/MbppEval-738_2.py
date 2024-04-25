def geometric_sum(n):
    sum = 0
    for i in range(n):
        sum += 1 / (2**i)
    return sum

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)