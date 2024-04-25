def find_solution(a, b, n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g = gcd(a, b)
    if n % g != 0:
        return 'No solution'

    x, y = extended_gcd(a, b)[1:]
    
    return 'x = ', x * (n // g), ', y = ', y * (n // g)

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)