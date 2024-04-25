import math

def sumofFactors(n):
    """
    Finds the sum of even factors of a number.

    Args:
        n (int): The number whose even factors need to be summed.

    Returns:
        int: The sum of even factors of the given number.
    """
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                total += i
            if (n // i) % 2 == 0 and (n // i) != i:
                total += n // i
    return total

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8

check(sumofFactors)