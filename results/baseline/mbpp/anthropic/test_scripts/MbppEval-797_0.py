def sum_odd(n):
    """
    Write a python function to find the sum of all odd natural numbers within the range l and r.

    Examples:
    sum_odd(2, 5) == 8
    sum_odd(5, 7) == 12
    sum_odd(7, 13) == 40
    """
    total = 0
    for num in range(n[0], n[1] + 1):
        if num % 2 != 0:
            total += num
    return total

def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)