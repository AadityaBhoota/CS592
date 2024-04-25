def move_num(test_str):
    # Create two empty strings to store the digits and non-digits
    digits = ""
    non_digits = ""

    # Iterate through each character in the input string
    for char in test_str:
        # Check if the character is a digit
        if char.isdigit():
            # If it is, append it to the digits string
            digits += char
        else:
            # If it's not, append it to the non-digits string
            non_digits += char

    # Concatenate the non-digits and digits strings and return the result
    return non_digits + digits

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)