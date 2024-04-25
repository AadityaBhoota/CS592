import calendar

def valid_date(date):
    if not isinstance(date, str) or len(date.split('-')) != 3:
        return False

    month_str, day_str, year_str = date.split('-')

    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        return False

    max_days = calendar.monthrange(year, month)[1]

    if day < 1 or day > max_days:
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