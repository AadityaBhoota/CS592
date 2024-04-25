import math

def count_divisors(n):
    """
    Checks whether the count of divisors of a given number is even or odd.

    Args:
        n (int): The number for which the divisor count is to be checked.

    Returns:
        str: "Even" if the count of divisors is even, "Odd" if the count is odd.
    """
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    
    if divisors % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)