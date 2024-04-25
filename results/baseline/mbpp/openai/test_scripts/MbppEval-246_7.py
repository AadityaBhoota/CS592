def babylonian_squareroot(number):
    x = number
    y = 1.0

    while abs(x - y) > 0.0000001:
        x = (x + y) / 2
        y = number / x

    return x

# Test cases




def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)