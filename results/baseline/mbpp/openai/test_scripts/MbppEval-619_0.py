def move_num(test_str):
    letters = []
    numbers = []

    # Separate letters and numbers
    for char in test_str:
        if char.isalpha():
            letters.append(char)
        elif char.isnumeric():
            numbers.append(char)

    # Combine letters and numbers
    result = ''.join(letters) + ''.join(numbers)

    return result

# Test cases




def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)