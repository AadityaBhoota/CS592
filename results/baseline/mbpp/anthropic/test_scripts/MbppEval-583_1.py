def catalan_number(n):
    """
    Calculates the nth Catalan number.

    The Catalan numbers are a sequence of natural numbers that occur in various
    counting problems, often involving recursively-defined objects.

    The nth Catalan number can be calculated using the formula:

    C_n = (2n)! / ((n+1)!*n!)

    where n! represents the factorial of n.

    Args:
        n (int): The index of the Catalan number to be calculated.

    Returns:
        int: The nth Catalan number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 1

    numerator = 1
    denominator = 1
    for i in range(1, n + 1):
        numerator *= 2 * i * (2 * i - 1)
        denominator *= i + 1

    return numerator // denominator

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)