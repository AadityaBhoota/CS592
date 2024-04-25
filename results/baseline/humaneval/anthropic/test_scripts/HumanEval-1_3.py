from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ''
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    result.append(current_group)
                    current_group = ''
        elif char == ' ':
            continue

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