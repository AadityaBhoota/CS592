import re

def is_decimal(num):
    """
    Write a function to check whether a given string is a decimal number with a precision of 2.

    Examples:
    is_decimal('123.11') == True
    is_decimal('e666.86') == False
    is_decimal('3.124587') == False
    """
    # Use a regular expression to check the input string
    pattern = r'^\d+\.\d{2}$'
    return bool(re.match(pattern, str(num)))

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)