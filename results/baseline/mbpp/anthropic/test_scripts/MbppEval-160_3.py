def find_solution(a, b, n):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.

    Examples:
    find_solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    find_solution(4, 2, 7) == 'No solution'
    find_solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
    """
    for x in range(n // a + 1):
        for y in range(n // b + 1):
            if a * x + b * y == n:
                return ('x = ', x, ', y = ', y)
    return 'No solution'

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)