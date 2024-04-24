def odd_num_sum(n):
    odd_num = 1
    total = 0
    
    for i in range(n):
        total += odd_num**4
        odd_num += 2

    return total

# Test cases




def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)