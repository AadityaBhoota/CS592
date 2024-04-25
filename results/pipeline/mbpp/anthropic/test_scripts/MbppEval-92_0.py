import re

def is_undulating(n):
    num_str = str(n)
    if len(num_str) < 2:
        return False
    for i in range(1, len(num_str)):
        if abs(int(num_str[i]) - int(num_str[i-1])) != 1:
            return False
    if not re.match(r"(12)+|(21)+", num_str):
        return False
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)