def check_monthnumb_number(monthnum2):
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    return monthnum2 in months_31_days

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)