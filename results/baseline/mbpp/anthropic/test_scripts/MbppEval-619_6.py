def move_num(test_str):
    # Create two empty strings to store the characters and numbers separately
    chars = ""
    nums = ""
    
    # Iterate through the input string
    for char in test_str:
        # Check if the current character is a digit
        if char.isdigit():
            # If it is, append it to the nums string
            nums += char
        else:
            # If it's not a digit, append it to the chars string
            chars += char
    
    # Concatenate the chars and nums strings and return the result
    return chars + nums

def check(candidate):
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'

check(move_num)