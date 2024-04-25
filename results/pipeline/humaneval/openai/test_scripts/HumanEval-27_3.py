def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char
    return new_string



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)