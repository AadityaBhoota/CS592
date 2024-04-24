def square_Sum(n):
    """
    Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.

    Examples:
    square_Sum(2) == 10
    square_Sum(3) == 35
    square_Sum(4) == 84
    """
    total_sum = 0
    for i in range(1, 2*n, 2):
        total_sum += i**2
    return total_sum

def check(candidate):
    assert square_Sum(2) == 10
    assert square_Sum(3) == 35
    assert square_Sum(4) == 84

check(square_Sum)