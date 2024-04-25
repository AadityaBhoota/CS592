import math

def is_polite(n):
    highest_power_of_2 = int(math.log(n, 2))
    polite_number = 2**highest_power_of_2 + 1
    return polite_number

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)