import re
def change_date_format(dt):
    date_parts = dt.split('-')
    day, month, year = date_parts[2], date_parts[1], date_parts[0]
    return f'{day}-{month}-{year}'

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)