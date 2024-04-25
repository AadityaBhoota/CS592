def babylonian_squareroot(number, tolerance=1e-10):
    """
    Compute the square root of a number using the Babylonian method.

    Args:
        number (float): The number to find the square root of.
        tolerance (float, optional): The desired precision of the result. Defaults to 1e-10.

    Returns:
        float: The square root of the input number.
    """
    if number < 0:
        raise ValueError("Input must be non-negative")

    # Initial guess
    x = number / 2

    # Iterate until the desired precision is reached
    while abs(x ** 2 - number) > tolerance:
        x = (x + number / x) / 2

    return x

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)