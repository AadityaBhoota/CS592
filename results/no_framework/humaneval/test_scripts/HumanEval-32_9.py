def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    leading_coefficient = max(xs, key=abs)
    if leading_coefficient == 0:
        return 0
    
    neg_xs = [-x for x in xs]
    possible_zeros = [i for i in range(-100, 101) if poly(neg_xs, i) == 0]
    zero = min(possible_zeros, key=lambda x: abs(x - 0.5))  # Choose the zero closest to 0.5 if multiple solutions
    return zero



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