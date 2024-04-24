def babylonian_squareroot(number):
    if number < 0:
        return None

    guess = number / 2.0
    tolerance = 0.0000001  # Set the tolerance for the calculations

    while abs(guess**2 - number) > tolerance:
        guess = (guess + number / guess) / 2.0

    return guess

# Test cases




def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)