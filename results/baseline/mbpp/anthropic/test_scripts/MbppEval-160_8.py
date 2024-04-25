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

    # Find the Bézout's coefficients x0 and y0
    x0, y0, _ = extended_gcd(a, b)

    # Calculate the solution
    x = x0 * (n // gcd(a, b))
    y = y0 * (n // gcd(a, b))

    return ("x = ", x, ", y = ", y)

def gcd(a, b):
    """
    Calculate the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Calculate the extended Euclidean algorithm to find the Bézout's coefficients.
    Returns x, y, and gcd(a, b), where ax + by = gcd(a, b).
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, d = extended_gcd(b, a % b)
        return y, x - (a // b) * y, d

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)