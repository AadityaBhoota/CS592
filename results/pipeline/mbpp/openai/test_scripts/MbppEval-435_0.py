def last_Digit(n) :
    '''
    Write a python function to find the last digit of a given number.

    Examples:
    last_Digit(123) == 3
    last_Digit(25) == 5
    last_Digit(30) == 0
    '''
def last_digit(n):
    # Step 1
    str_n = str(n)
    # Step 2
    return int(str_n[-1])

def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0

check(last_Digit)