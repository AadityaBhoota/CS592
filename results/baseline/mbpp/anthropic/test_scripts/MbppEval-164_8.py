import math

def div_sum(n):
    """
    Calculates the sum of divisors of a given number.

    Args:
        n (int): The number to find the divisor sum for.

    Returns:
        int: The sum of divisors of the given number.
    """
    divisor_sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum

def areEquivalent(a, b):
    """
    Determines if the sum of divisors of two integers are the same.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if the sum of divisors of a and b are the same, False otherwise.
    """
    return div_sum(a) == div_sum(b)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)