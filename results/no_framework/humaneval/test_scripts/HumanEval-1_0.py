def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    paren_string = paren_string.replace(' ', '')
    
    temp = []
    
    for char in paren_string:
        temp.append(char)
        if char == ')':
            result.append(''.join(temp))
            temp = []
    
    return result

# Test the function




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