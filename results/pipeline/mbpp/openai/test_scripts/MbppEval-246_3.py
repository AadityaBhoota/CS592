def babylonian_squareroot(number):
    guess = 1
    tolerance = 0.000001
    diff = tolerance + 1
    
    while diff > tolerance:
        new_guess = 0.5 * (guess + number / guess)
        diff = abs(guess - new_guess)
        guess = new_guess
        
    return guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)