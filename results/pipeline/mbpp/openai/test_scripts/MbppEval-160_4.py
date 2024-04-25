def find_solution(a, b, n):
    if a == 0:
        if b != 0 and n % b == 0:
            return (0, n // b)
        else:
            return None
    if b == 0:
        if a != 0 and n % a == 0:
            return (n // a, 0)
        else:
            return None

def check(candidate):
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)

check(find_solution)