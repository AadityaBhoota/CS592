def square_Sum(n):
    return n * (2 * n + 1) * (2 * n - 1) // 3

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)