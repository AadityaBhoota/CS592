def move_num(test_str):
    """
    Write a function to move all the numbers to the end of the given string.

    Examples:
    move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    move_num('Avengers124Assemble') == 'AvengersAssemble124'
    move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
    """
    # Split the string into characters
    chars = list(test_str)
    
    # Initialize two lists to store non-numeric and numeric characters
    non_numeric = []
    numeric = []
    
    # Iterate through the characters and append them to the appropriate list
    for char in chars:
        if char.isdigit():
            numeric.append(char)
        else:
            non_numeric.append(char)
    
    # Concatenate the non-numeric and numeric characters
    result = ''.join(non_numeric) + ''.join(numeric)
    
    return result

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)