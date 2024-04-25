def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients should be even")
    
    if all(coeff == 0 for coeff in xs):
        raise ValueError("All coefficients are zero")
    
    n = len(xs) - 1
    max_coeff = max(xs, key=abs)
    
    if n % 2 == 0:
        x = -max_coeff / xs[-2]
    else:
        x = -max_coeff / xs[-1]
    
    return x



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