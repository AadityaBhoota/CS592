def sum_digits(n):
    sum_of_digits = 0
    while n > 0:
        digit = n % 10
        sum_of_digits += digit
        n = n // 10
    return sum_of_digits

# Test cases




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)