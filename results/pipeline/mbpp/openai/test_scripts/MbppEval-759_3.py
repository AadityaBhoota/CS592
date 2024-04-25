def is_decimal(num):
    try:
        float_num = float(num)
        if '.' in num:
            integer_part, decimal_part = num.split('.')
            if len(decimal_part) == 2:
                return True
    except ValueError:
        pass
    return False

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)