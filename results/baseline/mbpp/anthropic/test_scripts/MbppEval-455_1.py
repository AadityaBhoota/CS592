def check_monthnumb_number(monthnum2):
    """
    Write a function to check whether the given month number contains 31 days or not.

    Examples:
    check_monthnumb_number(5) == True
    check_monthnumb_number(2) == False
    check_monthnumb_number(6) == False
    """
    # Months with 31 days
    months_31_days = [1, 3, 5, 7, 8, 10, 12]

    # Check if the given month number is in the list of months with 31 days
    if monthnum2 in months_31_days:
        return True
    else:
        return False

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)