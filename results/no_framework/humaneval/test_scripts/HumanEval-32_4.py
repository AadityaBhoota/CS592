import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    if len(xs) % 2 != 0 or len(xs) == 0:  # Check if xs has even number of coefficients
        raise ValueError("List must have an even number of coefficients.")

    # Find the largest non-zero coefficient
    largest_coeff = max([abs(coeff) for coeff in xs[1:]])

    # Start with an initial guess for x
    x = 0.0
    step = 0.1

    while True:
        if abs(poly(xs, x)) < 1e-6:  # Check if poly(x) is close to zero
            return x
        else:
            # Move towards zero using step size
            x -= math.copysign(step, poly(xs, x))
            # Adjust the step size based on the magnitude of the polynomial
            step = min(abs(step), 0.05 * largest_coeff)

# Test cases
print(find_zero([1, 2]))  # Output: -0.5
print(find_zero([-6, 11, -6, 1]))  # Output: 1.0



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