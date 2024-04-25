def find_solution(a, b, n):
    if n % gcd(a, b) != 0:
        return 'No solution'

    x0, y0 = find_particular_solution(a, b)

    x = x0 * (n // gcd(a, b))
    y = y0 * (n // gcd(a, b))

    return ('x = ', x, ', y = ', y)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_particular_solution(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = find_particular_solution(b, a % b)
        return y, x - (a // b) * y

# Testing the function




def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)