def sum_digits(n):
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return total_sum

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)