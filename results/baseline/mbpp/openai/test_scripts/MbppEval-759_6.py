def is_decimal(num):
    try:
        float_num = float(num)
        return round(float_num, 2) == float_num
    except ValueError:
        return False

# Test cases




def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)