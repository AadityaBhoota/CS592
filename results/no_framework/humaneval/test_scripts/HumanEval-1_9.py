from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    
    for char in paren_string:
        if char == '(':
            if stack:
                result.append(''.join(stack))
                stack = []
        
        stack.append(char)
        
        if char == ')':
            result.append(''.join(stack))
            stack = []
    
    return result

# Test the function with the example in the docstring


# Output: ['()', '(())', '(()())']



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