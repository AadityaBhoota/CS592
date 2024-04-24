def is_decimal(num):
    """
    Check whether a given string is a decimal number with a precision of 2.

    Examples:
    is_decimal('123.11') == True
    is_decimal('e666.86') == False
    is_decimal('3.124587') == False
    """
    try:
        float_num = float(num)
        return str(float_num).split('.')[1].isdigit() and len(str(float_num).split('.')[1]) == 2
    except ValueError:
        return False

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)