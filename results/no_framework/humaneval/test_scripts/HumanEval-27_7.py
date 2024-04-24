def flip_case(string: str) -> str:
    return ''.join([c.lower() if c.isupper() else c.upper() for c in string])

# Testing the function
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