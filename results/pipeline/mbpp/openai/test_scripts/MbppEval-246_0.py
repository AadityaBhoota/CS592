def babylonian_squareroot(number):
    guess = number/2
    precision = 0.0001
    while abs(guess*guess - number) > precision:
        guess = (guess + number/guess) / 2
    return guess

# Testing


def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)