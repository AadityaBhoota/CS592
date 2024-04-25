def square_Sum(n):  
    sum_squares = 0
    odd_number = 1

    for i in range(n):
        sum_squares += odd_number ** 2
        odd_number += 2

    return sum_squares

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)