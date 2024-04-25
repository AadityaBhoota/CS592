def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_solution(a, b, n):
    if a == 0 and b == 0:
        if n == 0:
            return ('x = ', 0, ', y = ', 0)
        else:
            return 'No solution'

    if a == 0:
        y = n // b
        return ('x = ', 0, ', y = ', y)

    if b == 0:
        x = n // a
        return ('x = ', x, ', y = ', 0)
    
    if a == 0 or b == 0:
        return 'No solution'

    if n % gcd(a, b) != 0:
        return 'No solution'

    gcd_val, x_gcd, y_gcd = extended_gcd(a, b)

    x_solution = x_gcd * (n // gcd(a, b))
    y_solution = y_gcd * (n // gcd(a, b))

    return ('x = ', x_solution, ', y = ', y_solution)

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)