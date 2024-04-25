def is_decimal(num):
    try:
        decimal_num = float(num)
        whole_part, decimal_part = str(decimal_num).split('.')
        
        if len(decimal_part) == 2:
            return True
        else:
            return False
    except ValueError:
        return False

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)