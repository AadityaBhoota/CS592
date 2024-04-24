import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even.")
    
    n = len(xs) - 1  # Degree of the polynomial

    def f(x):
        return poly(xs, x)
  
    def f_prime(x):
        return poly([i * xs[i] for i in range(1, n+1)], x)

    x0 = 0.0  # Initial guess
    max_iter = 100
    tol = 1e-7

    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1

    raise ValueError("No convergence in %d iterations." % max_iter)


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