def find_solution(a, b, n):
    for x in range(n // a + 1):
        y = (n - a * x) / b
        if y.is_integer():
            return 'x = {}, y = {}'.format(x, int(y))
    return 'No solution'

# Test cases




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)