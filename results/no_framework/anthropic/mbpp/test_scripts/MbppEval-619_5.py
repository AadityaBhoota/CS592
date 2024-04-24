def move_num(test_str):
    """
    Write a function to move all the numbers to the end of the given string.

    Examples:
    move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    move_num('Avengers124Assemble') == 'AvengersAssemble124'
    move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
    """
    # Separate the string into two lists: one for numbers and one for non-numbers
    nums = ''.join(char for char in test_str if char.isdigit())
    non_nums = ''.join(char for char in test_str if not char.isdigit())

    # Concatenate the non-numbers and the numbers
    return non_nums + nums

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)