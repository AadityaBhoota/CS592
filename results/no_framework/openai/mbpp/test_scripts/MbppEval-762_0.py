def check_monthnumber_number(monthnum):
    thirty_days_months = [4, 6, 9, 11]

    if monthnum in thirty_days_months:
        return True
    else:
        return False

# Testing the function




def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)