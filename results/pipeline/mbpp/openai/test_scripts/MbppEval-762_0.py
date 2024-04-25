def check_monthnumber_number(monthnum):
    if monthnum < 1 or monthnum > 12:
        return False
    
    if monthnum in [4, 6, 9, 11]:
        return True
    
    return False

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)