def move_num(test_str):
    # Extract all the numbers from the string
    numbers = ''.join(filter(str.isdigit, test_str))
    
    # Extract all the non-numeric characters
    non_numbers = ''.join(filter(lambda x: not x.isdigit(), test_str))
    
    # Concatenate the non-numeric characters and the numbers
    return non_numbers + numbers

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)