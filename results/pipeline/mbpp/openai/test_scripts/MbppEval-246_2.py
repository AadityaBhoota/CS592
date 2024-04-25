def babylonian_squareroot(number):
    guess = number / 2
    
    while True:
        improved_guess = (guess + number / guess) / 2
        if abs(improved_guess - guess) < 0.00001:  # Check if the guess is close enough to the actual square root
            return improved_guess
        guess = improved_guess

def check(candidate):
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

check(babylonian_squareroot)