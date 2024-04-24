def find_zero(xs: list):
    n = len(xs)
    if n % 2 != 0 or n == 0:
        raise ValueError("The number of coefficients must be even and non-zero.")

    # Since the largest non-zero coefficient guarantees a solution
    largest_non_zero = max([abs(coeff) for coeff in xs])
    if largest_non_zero == 0:
        return 0

    guess = -largest_non_zero
    while True:
        y = poly(xs, guess)
        if abs(y) < 1e-10:
            return guess

        # Update guess using Newton's method
        y_prime = poly_derivative(xs, guess)
        if y_prime == 0:
            return None
        guess = guess - y / y_prime

def poly_derivative(xs: list, x: float):
    """
    Evaluates the derivative of the polynomial with coefficients xs at point x.
    return derivative(xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i != 0])

# Example usage
print(round(find_zero([1, 2]), 2))  # Expecting: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # Expecting: 1.0



METADATA = {}


def check(candidate):
    import math
    import random
    rng = random.Random(42)
    import copy
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        solution = candidate(copy.deepcopy(coeffs))
        assert math.fabs(poly(coeffs, solution)) < 1e-4


check(find_zero)