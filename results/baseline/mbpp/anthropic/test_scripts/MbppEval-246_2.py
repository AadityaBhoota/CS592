def babylonian_squareroot(number, tolerance=1e-10):
    """
    Computes the square root of a number using the Babylonian method.

    Args:
        number (float): The number to compute the square root of.
        tolerance (float, optional): The desired level of accuracy. Defaults to 1e-10.

    Returns:
        float: The square root of the input number.
    """
    # Start with an initial guess
    x = number / 2

    # Iterate until the desired level of accuracy is reached
    while abs(x * x - number) > tolerance:
        x = (x + number / x) / 2

    return x

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)