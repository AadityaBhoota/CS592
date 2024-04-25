import math

def find_zero(xs: list):
    """
    Finds the zero point of a polynomial given its coefficients.
    The polynomial must have an even number of coefficients, and the largest non-zero
    coefficient must be the first one.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    for i in range(0, len(xs), 2):
        a = xs[i]
        b = xs[i+1]
        
        discriminant = b**2 - 4 * a * xs[i+2]
        if discriminant >= 0:
            x = (-b + math.sqrt(discriminant)) / (2 * a)
            return x
    
    raise ValueError("No zero point found.")



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