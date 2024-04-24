def check_monthnumb_number(monthnum2):
    # List of month numbers that have 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    if monthnum2 in months_with_31_days:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)