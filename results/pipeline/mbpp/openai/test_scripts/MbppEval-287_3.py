def square_Sum(n):  
    sum_squares = 0
    even_number = 2

    for i in range(n):
        square = even_number ** 2
        sum_squares += square
        even_number += 2

    return sum_squares

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120

check(square_Sum)