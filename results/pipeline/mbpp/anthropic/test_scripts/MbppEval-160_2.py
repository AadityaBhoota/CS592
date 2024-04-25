def extended_gcd(a, b):
    """
    Compute the extended Euclidean algorithm for a and b.
    Returns (gcd, x, y) such that ax + by = gcd(a, b)
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return 'No solution' if no solution exists.

    Examples:
    find_solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    find_solution(4, 2, 7) == 'No solution'
    find_solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
    """
    gcd, x, y = extended_gcd(a, b)
    if n % gcd != 0:
        return 'No solution'
    x0 = x * (n // gcd)
    y0 = y * (n // gcd)
    return ('x = ', x0, ', y = ', y0)

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)