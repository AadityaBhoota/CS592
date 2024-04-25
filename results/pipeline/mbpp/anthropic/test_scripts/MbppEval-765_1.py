import math

def is_polite(n):
    count = 0
    i = 1
    while count < n:
        if is_power_of_2(i) or is_sum_of_distinct_powers_of_2(i):
            count += 1
        i += 1
    return i - 1

def is_power_of_2(x):
    return (x & (x - 1)) == 0

def is_sum_of_distinct_powers_of_2(x):
    temp = x
    while temp > 0:
        if (temp & 1) == 1 and (temp & (temp - 1)) != 0:
            return False
        temp >>= 1
    return True

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)