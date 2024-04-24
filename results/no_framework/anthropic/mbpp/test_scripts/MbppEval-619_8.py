def move_num(test_str):
    """
    Write a function to move all the numbers to the end of the given string.

    Examples:
    move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    move_num('Avengers124Assemble') == 'AvengersAssemble124'
    move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
    """
    # Create two empty strings to store the non-numeric and numeric characters
    non_numeric = ""
    numeric = ""

    # Iterate through the input string
    for char in test_str:
        # Check if the character is a digit
        if char.isdigit():
            # If it is, append it to the numeric string
            numeric += char
        else:
            # If it's not a digit, append it to the non-numeric string
            non_numeric += char

    # Combine the non-numeric and numeric strings and return the result
    return non_numeric + numeric

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)