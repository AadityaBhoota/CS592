def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
        
    # Split the date string into its components
    date_components = date.split('-')
    
    # Check if the date string has three components
    if len(date_components) != 3:
        return False
    
    # Extract the month, day, and year from the date string
    month, day, year = date_components
    
    # Check if the month is between 1 and 12
    if not (1 <= int(month) <= 12):
        return False
    
    # Check the number of days based on the month
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        max_days = 31
    elif month in ['04', '06', '09', '11']:
        max_days = 30
    else:
        # Check for leap year in February
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            max_days = 29
        else:
            max_days = 28
            
    # Check if the day is between 1 and max_days
    if not (1 <= int(day) <= max_days):
        return False
    
    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False

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