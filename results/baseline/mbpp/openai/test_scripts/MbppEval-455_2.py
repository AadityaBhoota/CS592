def check_monthnumb_number(monthnum2):
    # Dictionary to map month numbers to the number of days in the month
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # Check if the month number is valid
    if monthnum2 in days_in_month:
        return days_in_month[monthnum2] == 31
    else:
        return False

# Test cases




def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)