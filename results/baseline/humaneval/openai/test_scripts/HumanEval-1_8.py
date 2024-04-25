from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    
    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                stack.pop()
            if not stack:
                result.append(''.join(stack))
    
    return result

# Test the function with the provided example




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