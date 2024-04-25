def next_power_of_2(n):
    if n <= 0:
        return 1
    if n & (n - 1) == 0:  # Check if n is already a power of 2
        return n
    else:
        return 2**(n.bit_length())

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)