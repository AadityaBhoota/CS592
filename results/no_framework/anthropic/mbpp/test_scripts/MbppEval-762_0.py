def check_monthnumber_number(monthnum):
    """
    Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.

    Examples:
    check_monthnumber_number(6) == True
    check_monthnumber_number(2) == False
    check_monthnumber_number(12) == False
    """
    thirty_day_months = [4, 6, 9, 11]
    if monthnum in thirty_day_months:
        return True
    else:
        return False

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)