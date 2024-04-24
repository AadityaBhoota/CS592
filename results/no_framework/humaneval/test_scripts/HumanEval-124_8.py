def valid_date(date):
    # Rule 1: The date string is not empty
    if len(date) == 0:
        return False

    # Rule 4: The date should be in the format: mm-dd-yyyy
    if not date.count('-') == 2:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    # Rule 3: The months should not be less than 1 or higher than 12
    if not 1 <= int(month) <= 12:
        return False

    # Rule 2: Validate the number of days based on the month
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= int(day) <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not 1 <= int(day) <= 30:
            return False
    elif month == '02':
        # Leap year check
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            if not 1 <= int(day) <= 29:
                return False
        else:
            if not 1 <= int(day) <= 28:
                return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))   # Output: False
print(valid_date('06-04-2020'))   # Output: True
print(valid_date('06/04/2020'))   # Output: False

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