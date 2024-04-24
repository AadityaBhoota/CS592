def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.

    Examples:
    find_solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    find_solution(4, 2, 7) == 'No solution'
    find_solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
    """
    # Check if a solution exists
    if n % gcd(a, b) != 0:
        return "No solution"

    # Find the extended Euclidean algorithm coefficients
    x, y, _ = extended_gcd(a, b)

    # Compute the particular solution
    x0 = x * (n // gcd(a, b))
    y0 = y * (n // gcd(a, b))

    return (f"x = ", x0, f", y = ", y0)

def gcd(a, b):
    """
    Compute the greatest common divisor of two integers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Compute the extended Euclidean algorithm coefficients x and y such that ax + by = gcd(a, b).
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y = a, r, u, v
        u, v = m, n
    return x, y, b

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)