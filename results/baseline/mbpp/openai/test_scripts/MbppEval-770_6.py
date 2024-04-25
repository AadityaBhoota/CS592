def odd_num_sum(n):
    return n**2 * (2*n**2 - 1)

# Test cases




def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)