def babylonian_squareroot(number, tolerance=1e-10):
    """
    Compute the square root of a number using the Babylonian method.

    Args:
        number (float): The number whose square root needs to be computed.
        tolerance (float, optional): The desired accuracy of the result. Defaults to 1e-10.

    Returns:
        float: The square root of the input number.
    """
    # Initialize the guess
    guess = number / 2

    # Iterate until the desired accuracy is reached
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)