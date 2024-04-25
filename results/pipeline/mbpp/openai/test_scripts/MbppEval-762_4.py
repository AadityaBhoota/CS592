def check_monthnumber_number(monthnum3):
    if not isinstance(monthnum3, int) or monthnum3 < 1 or monthnum3 > 12:
        return False
    elif monthnum3 in [4, 6, 9, 11]:
        return True
    return False

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)