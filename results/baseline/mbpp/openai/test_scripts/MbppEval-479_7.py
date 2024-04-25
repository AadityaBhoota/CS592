def first_Digit(n) :  
    '''
    Write a python function to find the first digit of a given number.

    Examples:
    first_Digit(123) == 1
    first_Digit(456) == 4
    first_Digit(12) == 1
    '''
def first_digit(n):
    # Convert the number to a string to easily access the first digit
    n_str = str(n)
    
    # Return the first character of the string, which is the first digit of the number
    return int(n_str[0])

# Test cases




def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)