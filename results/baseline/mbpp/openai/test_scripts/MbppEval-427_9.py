import re
def change_date_format(dt):
    '''
    Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

    Examples:
    change_date_format("2026-01-02") == '02-01-2026'
    change_date_format("2020-11-13") == '13-11-2020'
    change_date_format("2021-04-26") == '26-04-2021'
    '''
    # Split the date string by '-'
    year, month, day = dt.split('-')
    
    # Rearrange the date components to convert from yyyy-mm-dd format to dd-mm-yyyy format
    new_date = f'{day}-{month}-{year}'
    
    return new_date

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)