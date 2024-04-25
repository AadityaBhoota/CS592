import re

def change_date_format(dt):
    if not re.match(r'\d{4}-\d{2}-\d{2}', dt):
        return "Invalid date format. Please enter date in yyyy-mm-dd format."
    
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', dt)
    year, month, day = match.groups()
    
    new_date = f"{day}-{month}-{year}"
    
    return new_date

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)