from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    separate_groups = []
    open_paren_count = 0
    temp_group = ""

    for char in paren_string:
        temp_group += char
        if char == '(':
            open_paren_count += 1
        elif char == ')':
            open_paren_count -= 1
            if open_paren_count == 0:
                separate_groups.append(temp_group)
                temp_group = ""

    return separate_groups



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