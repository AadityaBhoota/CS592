def is_decimal(num):
    """
    Write a function to check whether a given string is a decimal number with a precision of 2.

    Examples:
    is_decimal('123.11') == True
    is_decimal('e666.86') == False
    is_decimal('3.124587') == False
    """
    if '.' not in num:
        return False

    parts = num.split('.')

    if not parts[0].isdigit():
        return False

    if len(parts[1]) != 2:
        return False

    return True

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)