def find_solution(a, b, n):
    # Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
    g, x, y = egcd(a, b)
    
    if n % g != 0:
        return 'No solution'
    
    x *= n // g
    y *= n // g
    
    return ('x = ', x, ', y = ', y)

# Test cases




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)