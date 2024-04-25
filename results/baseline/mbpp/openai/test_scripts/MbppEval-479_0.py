def first_Digit(n) :  
    '''
    Write a python function to find the first digit of a given number.

    Examples:
    first_Digit(123) == 1
    first_Digit(456) == 4
    first_Digit(12) == 1
    '''
def first_digit(n):
    if n == 0:
        return 0
    else:
        while n >= 10:
            n //= 10
        return n

# Test cases




def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)