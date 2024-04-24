def is_decimal(num):
    try:
        num = float(num)
        if round(num, 2) == num:
            return True
        return False
    except ValueError:
        return False

# Testing the function with examples




def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)