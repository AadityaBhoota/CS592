def is_decimal(num):
    if not isinstance(num, str):
        return False
    if not num.replace('.', '').isdigit() or num.count('.') != 1:
        return False
    parts = num.split('.')
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