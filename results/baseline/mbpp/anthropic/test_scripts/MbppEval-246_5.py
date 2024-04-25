def babylonian_squareroot(number, tolerance=1e-12):
    """
    Compute the square root of a number using the Babylonian method.

    Args:
        number (float): The number to find the square root of.
        tolerance (float): The desired precision of the result (default is 1e-12).

    Returns:
        float: The square root of the input number.
    """
    # Initialize the guess to the number itself
    guess = number

    # Iterate until the guess is within the desired tolerance
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)