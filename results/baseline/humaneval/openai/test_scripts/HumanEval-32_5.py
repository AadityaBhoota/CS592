def find_zero(xs: list):
    if len(xs) % 2 != 0 or len(xs) < 2:
        raise ValueError("The input list must have an even number of coefficients and at least two coefficients")

    # Find index of largest non zero coefficient
    index = max(range(len(xs)), key=lambda i: abs(xs[i]))

    # Set the leading coefficient to 1
    leading_coefficient = xs[index]
    normalized_xs = [coeff / leading_coefficient for coeff in xs]

    # Find roots using numpy's roots function
    import numpy as np
    roots = np.roots(normalized_xs)

    # Select the real root
    real_root = [root.real for root in roots if root.imag == 0][0]

    return real_root


# Test cases





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