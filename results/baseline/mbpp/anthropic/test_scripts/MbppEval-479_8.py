def first_Digit(n):
    """
    Write a python function to find the first digit of a given number.

    Examples:
    first_Digit(123) == 1
    first_Digit(456) == 4
    first_Digit(12) == 1
    """
    # Convert the number to a string and get the first character
    first_digit = str(n)[0]
    
    # Convert the first digit back to an integer and return it
    return int(first_digit)

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)