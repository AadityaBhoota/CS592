import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")

    # Find the largest non-zero coefficient
    max_coeff = max(abs(x) for x in xs)
    if max_coeff == 0:
        raise ValueError("All coefficients are zero, no solution exists.")

    # Find the index of the largest non-zero coefficient
    max_index = next(i for i, x in enumerate(xs) if abs(x) == max_coeff)

    # Solve the quadratic equation using the quadratic formula
    a = xs[max_index]
    b = xs[max_index - 1]
    c = sum(xs[:max_index - 1])

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real solutions exist.")
    elif discriminant == 0:
        return -b / (2*a)
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        return (-b + sqrt_discriminant) / (2*a)



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