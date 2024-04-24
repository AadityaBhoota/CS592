def find_solution(a, b, n):
    # Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    g, x, y = egcd(a, b)

    if n % g != 0:
        return 'No solution'

    k = n // g
    return 'x = {}, y = {}'.format(x*k, y*k)

# Test cases




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)