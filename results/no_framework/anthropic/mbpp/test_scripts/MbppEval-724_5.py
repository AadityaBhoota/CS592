def power_base_sum(base, power):
    """
    Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.

    Examples:
    power_base_sum(2,100) == 115
    power_base_sum(8,10) == 37
    power_base_sum(8,15) == 62
    """
    result = base ** power
    return sum(int(digit) for digit in str(result))

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
    assert power_base_sum(3,3)==9

check(power_base_sum)