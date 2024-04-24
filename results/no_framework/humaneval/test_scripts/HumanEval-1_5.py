from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    groups = []
    current_group = ""

    for char in paren_string:
        if char == "(":
            current_group += char
        elif char == ")":
            current_group += char
            groups.append(current_group)
            current_group = ""

    return groups


# Test the function
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [
        '(()())', '((()))', '()', '((())()())'
    ]
    assert candidate('() (()) ((())) (((())))') == [
        '()', '(())', '((()))', '(((())))'
    ]
    assert candidate('(()(())((())))') == [
        '(()(())((())))'
    ]
    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

check(separate_paren_groups)