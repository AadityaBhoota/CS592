def odd_num_sum(n):
    """
    Write a python function to find the sum of fourth power of first n odd natural numbers.

    Examples:
    odd_num_sum(2) == 82
    odd_num_sum(3) == 707
    odd_num_sum(4) == 3108
    """
    total = 0
    for i in range(1, 2*n, 2):
        total += i**4
    return total

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)