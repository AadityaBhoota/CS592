def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into components
    date_parts = date.split('-')

    # Check if there are exactly three components
    if len(date_parts) != 3:
        return False

    month, day, year = date_parts

    # Check if month, day, and year are numeric
    if not (month.isnumeric() and day.isnumeric() and year.isnumeric()):
        return False

    # Convert month and day to integers
    month = int(month)
    day = int(day)

    # Validate month range
    if month < 1 or month > 12:
        return False

    # Validate day range based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        # Check for leap year
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if day < 1 or day > 29
        else:
            if day < 1 or day > 28

    return True

# Test cases






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