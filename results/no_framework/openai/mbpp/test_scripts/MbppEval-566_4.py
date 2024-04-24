def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Test cases




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)