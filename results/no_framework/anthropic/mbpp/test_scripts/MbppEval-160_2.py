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
        return 'No solution'

    # Find the Bézout's coefficients
    x, y = extended_gcd(a, b)

    # Adjust the solution to satisfy the equation
    x = x * (n // gcd(a, b))
    y = y * (n // gcd(a, b))

    return ('x = ', x, ', y = ', y)

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Compute the Bézout's coefficients x and y such that ax + by = gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)