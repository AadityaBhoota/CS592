def is_decimal(num):
    if num.count('.') == 1:
        integer_part, decimal_part = num.split('.')
        if integer_part.isdigit() and decimal_part.isdigit() and len(decimal_part) == 2:
            return True
    return False

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)