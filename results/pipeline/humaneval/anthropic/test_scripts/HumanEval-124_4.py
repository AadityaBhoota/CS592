def valid_date(date):
    """
    Check if a given date string is valid.
    
    Args:
        date (str): The date string in the format "mm-dd-yyyy".
    
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Check if the input is empty
    if not date:
        return False
    
    # Split the date string into components
    parts = date.split('-')
    
    # Check if the date is in the correct format
    if len(parts) != 3:
        return False
    
    # Convert the components to integers
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    
    # Check the month value
    if month < 1 or month > 12:
        return False
    
    # Check the day value based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
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