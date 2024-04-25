import math

def perfect_squares(a, b):
    """
    Write a function to find perfect squares between two given numbers.

    Examples:
    perfect_squares(1, 30) == [1, 4, 9, 16, 25]
    perfect_squares(50, 100) == [64, 81, 100]
    perfect_squares(100, 200) == [100, 121, 144, 169, 196]
    """
    
    # Find the square root of the lower bound
    start = int(math.ceil(math.sqrt(a)))
    
    # Find the square root of the upper bound
    end = int(math.floor(math.sqrt(b)))
    
    # Calculate the perfect squares within the range
    return [i**2 for i in range(start, end + 1)]

def check(candidate):
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    assert perfect_squares(50,100)==[64, 81, 100]
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]

check(perfect_squares)