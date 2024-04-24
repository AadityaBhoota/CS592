def find_zero(xs: list, tol=1e-6):
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have an even number of coefficients.")

    def poly_to_solve(x):
        return poly(xs, x)

    a = -1000  # Initial guess for lower bound
    b = 1000  # Initial guess for upper bound

    # Iterate until the interval is small enough
    while b - a > tol:
        mid = (a + b) / 2
        if poly_to_solve(mid) == 0:
            return mid
        elif poly_to_solve(a) * poly_to_solve(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2



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