def find_solution(a, b, n):
    # Check if a and b are both 0
    if a == 0 and b == 0:
        return None
    
    # Check if a and b are both 0 and n is also 0
    if a == 0 and b == 0 and n == 0:
        return ('x = ', 0, ', y = ', 0)
    
    # Use Extended Euclidean Algorithm to find solution
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = extended_gcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = extended_gcd(a, b)
    
    # Check if g divides n
    if n % g != 0:
        return 'No solution'
    
    # Calculate x and y
    x *= n // g
    y *= n // g
    
    return ('x = ', x, ', y = ', y)

# Test cases




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)