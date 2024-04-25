def square_Sum(n):
    total = 0
    for i in range(1, n+1):
        total += (2 * i - 1) ** 2
    return total

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)