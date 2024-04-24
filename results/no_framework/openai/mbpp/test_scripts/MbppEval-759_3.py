import re

def is_decimal(num):
    pattern = r'^\d+\.\d{2}$'
    return bool(re.match(pattern, num))

# Test cases




def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
    assert is_decimal('1.11')==True
    assert is_decimal('1.1.11')==False

check(is_decimal)