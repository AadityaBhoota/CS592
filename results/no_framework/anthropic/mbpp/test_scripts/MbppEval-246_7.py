def babylonian_squareroot(number, tolerance=1e-10):
    """
    Computes the square root of a number using the Babylonian method.

    Args:
        number (float): The number whose square root is to be computed.
        tolerance (float): The desired level of precision for the result (default is 1e-10).

    Returns:
        float: The square root of the input number.
    """
    if number < 0:
        raise ValueError("Input must be a non-negative number.")

    # Initialize the guess to be half the input number
    guess = number / 2

    # Iterate until the guess is within the desired tolerance
    while abs(guess**2 - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)