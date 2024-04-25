def check_monthnumber_number(monthnum3):
    if 1 <= monthnum3 <= 12:
        if monthnum3 in [4, 6, 9, 11]:
            return True
        else:
            return False
    return False

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)