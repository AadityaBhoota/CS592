def sum_of_common_divisors(a, b):
    """
    Write a python function to find the sum of common divisors of two given numbers.

    Examples:
    sum_of_common_divisors(10, 15) == 6
    sum_of_common_divisors(100, 150) == 93
    sum_of_common_divisors(4, 6) == 3
    """
    # Find the common divisors of a and b
    common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

    # Calculate the sum of common divisors
    return sum(common_divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)