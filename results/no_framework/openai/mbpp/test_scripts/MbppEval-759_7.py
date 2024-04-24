def is_decimal(num):
    try:
        num = float(num)
    except ValueError:
        return False
    return round(num, 2) == num

# Test cases




def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)