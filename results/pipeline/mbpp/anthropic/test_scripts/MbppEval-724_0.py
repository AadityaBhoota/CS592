def power_base_sum(base, power):
    result = base ** power
    total_sum = 0
    for digit in str(result):
        total_sum += int(digit)
    return total_sum

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
    assert power_base_sum(3,3)==9

check(power_base_sum)