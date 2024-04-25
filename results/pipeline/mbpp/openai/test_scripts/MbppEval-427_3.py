import re

def change_date_format(dt):
    # Step 1: Use regex to match year, month, and day from input date
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", dt)
    if match:
        year, month, day = match.groups()
        
        # Step 2: Rearrange matched elements to form the desired format 'dd-mm-yyyy'
        new_date = f"{day}-{month}-{year}"
        
        # Step 3: Return the converted date
        return new_date

def check(candidate):
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2020-11-13") == '13-11-2020'
    assert change_date_format("2021-04-26") == '26-04-2021'

check(change_date_format)