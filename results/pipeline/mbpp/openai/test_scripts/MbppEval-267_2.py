def square_Sum(n):
    sum_squares = 0

    for i in range(1, 2*n+1, 2):
        square = i * i
        sum_squares += square

    return sum_squares

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)