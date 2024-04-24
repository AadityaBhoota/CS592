def babylonian_squareroot(number):
    if number < 0:
        return None

    x = number
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + number / x) // 2
    return x

# Test cases




def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)