import math

def count_divisors(n):
    divisor_count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                divisor_count += 1
            else:
                divisor_count += 2

    if divisor_count % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test cases




def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)