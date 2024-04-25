def sum_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)