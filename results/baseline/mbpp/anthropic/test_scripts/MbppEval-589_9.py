def perfect_squares(a, b):
    """
    Write a function to find perfect squares between two given numbers.

    Examples:
    perfect_squares(1,30) == [1, 4, 9, 16, 25]
    perfect_squares(50,100) == [64, 81, 100]
    perfect_squares(100,200) == [100, 121, 144, 169, 196]
    """
    return [x**2 for x in range(int(a ** 0.5), int(b ** 0.5) + 1)]

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)