def move_num(test_str):
    numbers = []
    non_numbers = []

    for char in test_str:
        if char.isnumeric():
            numbers.append(char)
        else:
            non_numbers.append(char)

    return ''.join(non_numbers + numbers)

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)