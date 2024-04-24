def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

# Test cases




def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16

check(sum_digits)