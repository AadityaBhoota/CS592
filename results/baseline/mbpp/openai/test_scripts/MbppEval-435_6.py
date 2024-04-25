def last_Digit(n) :
    '''
    Write a python function to find the last digit of a given number.

    Examples:
    last_Digit(123) == 3
    last_Digit(25) == 5
    last_Digit(30) == 0
    '''
def last_digit(n):
    return n % 10

# Test cases




def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0

check(last_Digit)