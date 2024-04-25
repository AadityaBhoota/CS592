def square_Sum(n):
    total = 0
    i = 1
    for _ in range(n):
        total += i**2
        i += 2
    return total

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)