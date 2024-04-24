    def f(x):
        return poly(xs, x)

    def df(x):
        h = 1e-9
        return (f(x + h) - f(x)) / h

    def find_zero(xs):
        if len(xs) % 2 != 0:
            raise ValueError("Even number of coefficients required")
        if max(xs, key=abs) == 0:
            raise ValueError("Largest non-zero coefficient should be non-zero")

        max_iter = 1000
        x = 0.0
        for i in range(max_iter):
            x = x - f(x) / df(x)
            if abs(f(x)) < 1e-9:
                break

        return x

    # Testing the find_zero function
    print(round(find_zero([1, 2]), 2))  # Output: -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Output: 1.0



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