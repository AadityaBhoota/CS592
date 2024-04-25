def babylonian_squareroot(number, tolerance=1e-10):
    """
    Compute the square root of a given number using the Babylonian method.

    Args:
        number (float): The number to find the square root of.
        tolerance (float): The desired accuracy of the result (default is 1e-10).

    Returns:
        float: The square root of the input number.
    """
    if number < 0:
        raise ValueError("Input number must be non-negative.")

    # Initialize the guess
    guess = number / 2

    # Iterate until the desired tolerance is reached
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)