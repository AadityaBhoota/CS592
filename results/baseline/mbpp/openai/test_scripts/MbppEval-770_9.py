def odd_num_sum(n):
    sum = n * (2*n-1) * (2*n-1) * (2*n-1) 
    return sum

# Test cases




def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)