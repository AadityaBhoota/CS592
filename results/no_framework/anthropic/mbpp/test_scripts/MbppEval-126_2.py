def sum_common_divisors(a, b):
    """
    Find the sum of common divisors of two given numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of common divisors of `a` and `b`.
    """
    divisors_a = set()
    divisors_b = set()

    # Find all divisors of a
    for i in range(1, a + 1):
        if a % i == 0:
            divisors_a.add(i)

    # Find all divisors of b
    for i in range(1, b + 1):
        if b % i == 0:
            divisors_b.add(i)

    # Find the common divisors
    common_divisors = divisors_a.intersection(divisors_b)

    # Calculate the sum of common divisors
    return sum(common_divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)