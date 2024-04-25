import math

def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must not be zero.")
    
    def poly(x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    x0 = 0  # Initial guess for the zero
    tolerance = 1e-8  # Tolerance for convergence
    max_iterations = 100  # Maximum number of iterations
    i = 0
    while i < max_iterations:
        fx0 = poly(x0)
        if abs(fx0) < tolerance:
            return x0
        dfx0 = sum([i * coeff * math.pow(x0, i - 1) for i, coeff in enumerate(xs) if i > 0])
        x0 = x0 - fx0 / dfx0
        i += 1

    raise ValueError("Could not find a zero within the maximum number of iterations.")



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