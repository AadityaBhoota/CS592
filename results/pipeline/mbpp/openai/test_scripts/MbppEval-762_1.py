def check_monthnumber_number(monthnum):
    thirty_day_months = [4, 6, 9, 11]  # April, June, September, and November have 30 days
    
    return monthnum in thirty_day_months

# Testing the function




def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)