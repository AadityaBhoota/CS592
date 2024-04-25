def odd_num_sum(n):
    if n <= 0:
        return 0
    else:
        return sum([(2*i+1)**4 for i in range(n)])

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)