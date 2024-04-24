def square_Sum(n):
    sum_square = 0
    for i in range(1, n*2 + 1, 2):
        sum_square += i**2
    return sum_square

# Test cases




def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)