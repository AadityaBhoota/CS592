def gcd(a, b):
    """
    Find the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b, n):
    """
    Find the extended Euclidean algorithm to solve ax + by = n.
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, d = extended_gcd(b, a % b, n)
        return y, x - (a // b) * y, d

def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
    """
    d = gcd(a, b)
    if n % d != 0:
        return None
    
    x, y, _ = extended_gcd(a // d, b // d, n // d)
    return (x, y)

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)