def odd_num_sum(n):
    sum_of_fourth_power = 0
    for i in range(1, n+1, 2):
        sum_of_fourth_power += i ** 4
    return sum_of_fourth_power

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)