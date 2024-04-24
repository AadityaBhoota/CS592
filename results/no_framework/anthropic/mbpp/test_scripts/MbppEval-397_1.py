def median_numbers(a, b, c):
    """
    Write a function to find the median of three numbers.

    Examples:
    median_numbers(25, 55, 65) == 55.0
    median_numbers(20, 10, 30) == 20.0
    median_numbers(15, 45, 75) == 45.0
    """
    return sorted([a, b, c])[1]

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)