def find_solution(a, b, n):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    gcd, x0, y0 = extended_gcd(a, b)

    if n % gcd != 0:
        return 'No solution'

    x = x0 * (n // gcd)
    y = y0 * (n // gcd)

    return ('x = ', x, ', y = ', y)

# Test cases




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)