def power_base_sum(base, power):
    result = base ** power
    sum_of_digits = sum(int(digit) for digit in str(result))
    return sum_of_digits

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
    assert power_base_sum(3,3)==9

check(power_base_sum)