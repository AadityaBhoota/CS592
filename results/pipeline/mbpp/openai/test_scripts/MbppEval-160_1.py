def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def find_solution(a, b, n):
    if a == 0 and b == 0:
        return 'No solution'

    if a == 0:
        if n % b == 0:
            return 'x = 0, y = {}'.format(n // b)
        else:
            return 'No solution'

    if b == 0:
        if n % a == 0:
            return 'x = {}, y = 0'.format(n // a)
        else:
            return 'No solution'

    g, x, y = extended_gcd(a, b)

    if n % g == 0:
        x *= n // g
        y *= n // g
        return 'x = {}, y = {}'.format(x, y)
    else:
        return 'No solution'

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)