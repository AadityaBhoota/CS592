def power_base_sum(base, power):
    result = base ** power
    result_str = str(result)
    sum_of_digits = 0
    for digit in result_str:
        sum_of_digits += int(digit)
    return sum_of_digits

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
    assert power_base_sum(3,3)==9

check(power_base_sum)