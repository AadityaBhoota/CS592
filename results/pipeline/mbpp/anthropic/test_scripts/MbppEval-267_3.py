def square_Sum(n):
    total_sum = 0
    for i in range(1, 2*n, 2):
        total_sum += i**2
    return total_sum

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)