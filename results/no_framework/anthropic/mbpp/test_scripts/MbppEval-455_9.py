def check_monthnumb_number(monthnum):
    """
    Write a function to check whether the given month number contains 31 days or not.

    Examples:
    check_monthnumb_number(5) == True
    check_monthnumb_number(2) == False
    check_monthnumb_number(6) == False
    """
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return monthnum in months_with_31_days

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)