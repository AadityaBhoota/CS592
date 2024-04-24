def flip_case(string: str) -> str:
    flipped_string = ''
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        elif char.isupper():
            flipped_string += char.lower()
        else:
            flipped_string += char
    return flipped_string

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)