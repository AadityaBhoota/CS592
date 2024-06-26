def is_decimal(num):
    """
    Write a function to check whether a given string is a decimal number with a precision of 2.

    Examples:
    is_decimal('123.11') == True
    is_decimal('e666.86') == False
    is_decimal('3.124587') == False
    """
    if '.' in num and num.replace('.', '').isdigit():
        decimal_part = num.split('.')[1]
        if len(decimal_part) == 2:
            return True
    return False

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)