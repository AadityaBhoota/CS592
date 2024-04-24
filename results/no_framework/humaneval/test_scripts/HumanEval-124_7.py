def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into parts
    parts = date.split('-')

    if len(parts) != 3:
        return False

    # Extract month, day, and year from the date string
    month, day, year = parts

    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Check if the month is valid
    if month < 1 or month > 12:
        return False

    # Check if the day is within the valid range for each month
    if (month in [1, 3, 5, 7, 8, 10, 12) and (day < 1 or day > 31):
        return False
    elif (month in [4, 6, 9, 11) and (day < 1 or day > 30):
        return False
    elif (month == 2) and (day < 1 or day > 29):
        return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))   # True
print(valid_date('06/04/2020'))   # False

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