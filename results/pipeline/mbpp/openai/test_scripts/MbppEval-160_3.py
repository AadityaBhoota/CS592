from math import gcd

def find_solution(a, b, n):
    if a == 0 or b == 0:
        return None
    
    if n % gcd(a, b) != 0:
        return 'No solution'

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd_val, x0, y0 = extended_gcd(a, b)

    multiplier = n // gcd(a, b)
    x = x0 * multiplier
    y = y0 * multiplier
    
    return ('x =', x, ', y =', y)

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)