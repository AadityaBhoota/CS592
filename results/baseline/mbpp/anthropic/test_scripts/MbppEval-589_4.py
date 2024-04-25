import math

def perfect_squares(a, b):
    """
    Write a function to find perfect squares between two given numbers.

    Examples:
    perfect_squares(1, 30) == [1, 4, 9, 16, 25]
    perfect_squares(50, 100) == [64, 81, 100]
    perfect_squares(100, 200) == [100, 121, 144, 169, 196]
    """
    result = []
    for i in range(a, b + 1):
        sqrt = int(math.sqrt(i))
        if sqrt * sqrt == i:
            result.append(i)
    return result

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)