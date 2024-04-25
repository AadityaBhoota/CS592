def next_power_of_2(n): 
    if n <= 0:
        return 1
    p = 1
    while p < n:
        p *= 2
    return p

# Test cases




def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)