def catalan_number(num):
    """
    Returns the nth Catalan number.

    Args:
        num (int): The index of the Catalan number to calculate.

    Returns:
        int: The nth Catalan number.
    """
    def factorial(n):
        """Helper function to calculate the factorial of a number."""
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    numerator = factorial(2*num)
    denominator = factorial(num+1) * factorial(num)
    return numerator // denominator

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)