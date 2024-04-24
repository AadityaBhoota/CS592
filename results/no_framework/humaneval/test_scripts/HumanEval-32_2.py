import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    max_coeff = max(xs, key=abs)
    xs_normalized = [coeff / max_coeff for coeff in xs]
    
    for x in range(-1000, 1001):
        if math.isclose(poly(xs_normalized, x), 0, abs_tol=1e-9):
            return round(x * max_coeff, 2)
    
    raise ValueError("No zero found within the range.")

# Test cases
print(round(find_zero([1, 2]), 2))  # Should output -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # Should output 1.0



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