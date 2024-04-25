from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    separate_groups = []
    stack = []
    open_index = -1
    
    paren_string = paren_string.replace(" ", "")
    
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            open_index = stack.pop()
            group = paren_string[open_index:i + 1]
            separate_groups.append(group)
    
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