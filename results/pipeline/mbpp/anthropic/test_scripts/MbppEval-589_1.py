import math

def perfect_squares(a, b):
    """
    Write a function to find perfect squares between two given numbers.

    Examples:
    perfect_squares(1,30) == [1, 4, 9, 16, 25]
    perfect_squares(50,100) == [64, 81, 100]
    perfect_squares(100,200) == [100, 121, 144, 169, 196]
    """
    if not (isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        raise ValueError("a and b must be positive integers")

    perfect_squares_list = []

    for num in range(a, b+1):
        sqrt = math.sqrt(num)
        if sqrt.is_integer():
            perfect_squares_list.append(num)

    return perfect_squares_list

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)