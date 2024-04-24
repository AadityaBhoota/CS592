def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # Remove any spaces in the input string
    result = []
    
    # Initialize a variable to keep track of current group
    current_group = ""
    
    for char in paren_string:
        current_group += char
        if current_group.count('(') == current_group.count(')'):
            result.append(current_group)
            current_group = ""
    
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