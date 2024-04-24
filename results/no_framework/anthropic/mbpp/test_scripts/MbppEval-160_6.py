def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.

    Examples:
    find_solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    find_solution(4, 2, 7) == 'No solution'
    find_solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
    """
    
    # Check if a solution exists
    if n % gcd(a, b) != 0:
        return "No solution"
    
    # Find the solution
    x, y = 0, 0
    for i in range(abs(n // a) + 1):
        for j in range(abs(n // b) + 1):
            if a * i + b * j == n:
                x, y = i, j
                return ("x = ", x, ", y = ", y)
    
    return None

def gcd(a, b):
    """
    Computes the greatest common divisor of two integers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)