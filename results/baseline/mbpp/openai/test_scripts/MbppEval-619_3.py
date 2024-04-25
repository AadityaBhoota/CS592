def move_num(test_str):
    # Initialize variables to store alphabets and numbers
    alphabets = []
    numbers = []

    # Separate alphabets and numbers from the input string
    for char in test_str:
        if char.isnumeric():
            numbers.append(char)
        else:
            alphabets.append(char)

    # Concatenate alphabets and numbers to form the final string
    result = ''.join(alphabets) + ''.join(numbers)

    return result

# Test the function with examples




def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)