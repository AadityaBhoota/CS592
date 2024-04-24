def square_Sum(n):
    sum_squares = sum([i**2 for i in range(2, 2*n+1, 2)])
    return sum_squares

# Test cases




def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)