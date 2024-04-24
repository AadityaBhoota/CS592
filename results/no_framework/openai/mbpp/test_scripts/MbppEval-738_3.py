def geometric_sum(n):
    if n == 0:
        return 1
    else:
        return 1 + 1/2**n + geometric_sum(n - 1)

# Test cases




def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)