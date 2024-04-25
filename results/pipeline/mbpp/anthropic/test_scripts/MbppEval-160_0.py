def find_solution(a, b, n):
    """
    Returns integers x and y that satisfy ax + by = n as a tuple, or None if no solution exists.
    """
    def gcd(x, y):
        """Compute the greatest common divisor of x and y."""
        while y != 0:
            x, y = y, x % y
        return x

    def extended_euclidean(a, b):
        """
        Compute the extended Euclidean algorithm for a and b.
        Returns x, y, and gcd(a, b), where ax + by = gcd(a, b).
        """
        if b == 0:
            return 1, 0, a
        else:
            x, y, d = extended_euclidean(b, a % b)
            return y, x - (a // b) * y, d

    d = gcd(a, b)
    if n % d != 0:
        return None

    x0, y0, _ = extended_euclidean(a // d, b // d)
    x = x0 * (n // d)
    y = y0 * (n // d)
    return (f"x = {x}", f"y = {y}")

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)