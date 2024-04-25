def check_monthnumb_number(monthnum2):
    if monthnum2 < 1 or monthnum2 > 12:
        return False

    days_in_month = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31}

    if monthnum2 in days_in_month.keys() and days_in_month[monthnum2] == 31:
        return True
    else:
        return False

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)