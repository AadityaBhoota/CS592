def check_monthnumb_number(monthnum2):
    thirty_one_days_months = [1, 3, 5, 7, 8, 10, 12]
    
    if monthnum2 in thirty_one_days_months:
        return True
    else:
        return False

# Test the function




def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)