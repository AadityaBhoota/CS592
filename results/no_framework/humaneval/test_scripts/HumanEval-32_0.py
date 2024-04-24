import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have an even number of coefficients")

    n = len(xs) - 1
    largest_coeff = max(xs, key=abs)
    x = -largest_coeff / xs[-1]

    return x


# Testing the find_zero function with the provided examples
print(round(find_zero([1, 2]), 2))  # Output should be approximately -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # Output should be approximately 1.0



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