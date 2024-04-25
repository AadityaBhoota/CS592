from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ""
    open_count = 0
    close_count = 0

    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group += char
        elif char == ')':
            close_count += 1
            current_group += char
        else:  # Ignore spaces
            continue

        if open_count == close_count:
            result.append(current_group)
            current_group = ""
            open_count = 0
            close_count = 0

    if current_group:
        result.append(current_group)

    return result



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