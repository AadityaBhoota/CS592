import re

def change_date_format(dt):
    '''
    Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

    Examples:
    change_date_format("2026-01-02") == '02-01-2026'
    change_date_format("2020-11-13") == '13-11-2020'
    change_date_format("2021-04-26") == '26-04-2021'
    '''
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", dt)
    if match:
        year, month, day = match.groups()
        return f"{day}-{month}-{year}"
    else:
        raise ValueError("Invalid date format: {dt}")

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)