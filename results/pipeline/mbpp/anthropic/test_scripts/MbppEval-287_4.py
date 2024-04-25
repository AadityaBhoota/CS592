def square_Sum(n):
    sum_of_squares = 0
    for i in range(1, n+1):
        even_number = i * 2
        sum_of_squares += even_number ** 2
    return sum_of_squares

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)