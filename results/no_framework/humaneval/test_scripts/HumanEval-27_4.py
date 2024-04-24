def flip_case(string: str) -> str:
    flipped = ''
    for char in string:
        if char.islower():
            flipped += char.upper()
        elif char.isupper():
            flipped += char.lower()
        else:
            flipped += char
    return flipped

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)