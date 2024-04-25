def square_Sum(n):
    sum_of_squares = 0
    for i in range(1, 2*n, 2):
        sum_of_squares += i**2
    return sum_of_squares

# Test cases




def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)