def check_monthnumb_number(monthnum2):
    if monthnum2 < 1 or monthnum2 > 12:
        return False
    
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}

    if monthnum2 in months_with_31_days:
        return True
    else:
        return False

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)