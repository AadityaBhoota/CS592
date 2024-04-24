def sum_common_divisors(a, b):
    """
    Find the sum of common divisors of two given numbers.

    Examples:
    sum_common_divisors(10, 15) == 6
    sum_common_divisors(100, 150) == 93
    sum_common_divisors(4, 6) == 3
    """
    divisors = set()
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.add(i)
    return sum(divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)