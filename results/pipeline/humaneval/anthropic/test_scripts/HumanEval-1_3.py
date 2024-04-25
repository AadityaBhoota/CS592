from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = ""
    nesting_level = 0
    
    for char in paren_string:
        if char == '(':
            nesting_level += 1
            current_group += char
        elif char == ')':
            nesting_level -= 1
            current_group += char
            if nesting_level == 0:
                groups.append(current_group)
                current_group = ""
        elif char != ' ':
            current_group += char
    
    return groups



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