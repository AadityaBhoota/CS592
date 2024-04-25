import calendar

def check_monthnumb_number(month, year):
    _, num_days = calendar.monthrange(year, month)
    return num_days == 31

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False

check(check_monthnumb_number)