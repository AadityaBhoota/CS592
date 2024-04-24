def babylonian_squareroot(number):
    guess = number / 2
    tolerance = 0.0000001  # defines the precision of the result
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2
    return guess

# Test the function




def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)