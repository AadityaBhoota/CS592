def valid_date(date):
    if not date:
        return False
    
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    
    month, day, year = date_parts
    
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False
    
    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28
    
    if day < 1 or day > max_days:
        return False
    
    if year <= 0:
        return False

    return True

def check(candidate):

    # Check some simple cases
    assert candidate('03-11-2000') == True

    assert candidate('15-01-2012') == False

    assert candidate('04-0-2040') == False

    assert candidate('06-04-2020') == True

    assert candidate('01-01-2007') == True

    assert candidate('03-32-2011') == False

    assert candidate('') == False

    assert candidate('04-31-3000') == False

    assert candidate('06-06-2005') == True

    assert candidate('21-31-2000') == False

    assert candidate('04-12-2003') == True

    assert candidate('04122003') == False

    assert candidate('20030412') == False

    assert candidate('2003-04') == False

    assert candidate('2003-04-12') == False

    assert candidate('04-2003') == False

check(valid_date)