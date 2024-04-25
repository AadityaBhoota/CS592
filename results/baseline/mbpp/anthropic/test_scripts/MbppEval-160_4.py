def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.

    Examples:
    find_solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    find_solution(4, 2, 7) == 'No solution'
    find_solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
    """
    # Check if a and b are both zero
    if a == 0 and b == 0:
        if n == 0:
            return ('x = ', 0, ', y = ', 0)
        else:
            return 'No solution'

    # Check if a is zero
    if a == 0:
        if n % b == 0:
            return ('x = ', 0, ', y = ', n // b)
        else:
            return 'No solution'

    # Check if b is zero
    if b == 0:
        if n % a == 0:
            return ('x = ', n // a, ', y = ', 0)
        else:
            return 'No solution'

    # Try to find a solution using the extended Euclidean algorithm
    x, y, gcd = extended_euclidean(a, b)

    # Check if n is divisible by the GCD
    if n % gcd != 0:
        return 'No solution'

    # Adjust the solution to satisfy the equation
    k = n // gcd
    return ('x = ', x * k, ', y = ', y * k)

def extended_euclidean(a, b):
    """
    Implements the extended Euclidean algorithm to find the greatest common divisor (GCD)
    of two integers a and b, as well as the coefficients x and y that satisfy the Bézout's identity:
    ax + by = gcd(a, b)
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_euclidean(b, a % b)
        return y, x - (a // b) * y, gcd

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)