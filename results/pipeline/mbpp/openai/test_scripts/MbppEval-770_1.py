def odd_num_sum(n):
    sum_odd = 0

    for i in range(1, 2*n, 2):  
        sum_odd += i ** 4

    return sum_odd

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)