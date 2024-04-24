def move_num(test_str):
    """
    Write a function to move all the numbers to the end of the given string.

    Examples:
    move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    move_num('Avengers124Assemble') == 'AvengersAssemble124'
    move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
    """
    num_part = ''.join(filter(str.isdigit, test_str))
    alpha_part = ''.join(filter(str.isalpha, test_str))
    return alpha_part + num_part


def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)