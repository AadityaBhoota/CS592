def check_monthnumber_number(monthnum3):
    months_with_30_days = [4, 6, 9, 11]
    return monthnum3 in months_with_30_days

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False

check(check_monthnumber_number)