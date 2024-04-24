def is_perfect_square(n):
    """
    Checks whether the given number is a perfect square or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        # Use the fact that a perfect square has an odd number of factors
        # If the number of factors is odd, then it is a perfect square
        factors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                factors += 1
        return factors % 2 == 1

def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)