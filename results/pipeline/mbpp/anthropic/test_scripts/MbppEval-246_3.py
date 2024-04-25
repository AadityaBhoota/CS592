def babylonian_squareroot(number):
    """
    Write a function for computing square roots using the Babylonian method.

    Examples:
    babylonian_squareroot(10) == 3.162277660168379
    babylonian_squareroot(2) == 1.414213562373095
    babylonian_squareroot(9) == 3.0
    """
    guess = (1 + number) / 2
    
    while abs(guess**2 - number) >= 0.000001:
        guess = (guess + number/guess) / 2
    
    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)