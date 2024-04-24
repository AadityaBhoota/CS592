def sum_of_common_divisors(a, b):
    """
    Finds the sum of common divisors of two given numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of common divisors of `a` and `b`.
    """
    divisors = set()

    # Find all the common divisors of a and b
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.add(i)

    # Calculate the sum of the common divisors
    return sum(divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)