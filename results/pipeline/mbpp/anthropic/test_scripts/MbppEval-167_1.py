def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()

def check(candidate):
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

check(next_power_of_2)