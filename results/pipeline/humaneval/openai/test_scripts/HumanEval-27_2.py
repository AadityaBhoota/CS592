def flip_case(string: str) -> str:
    flipped_string = ""
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        elif char.islower():
            flipped_string += char.upper()
    return flipped_string



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)