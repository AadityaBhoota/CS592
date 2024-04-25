from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    separated_groups = []
    left = 0
    right = 0
    start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            left += 1
        elif char == ')':
            right += 1
        
        if left == right:
            separated_groups.append(paren_string[start:(i+1)])
            start = i + 1
    
    return separated_groups



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