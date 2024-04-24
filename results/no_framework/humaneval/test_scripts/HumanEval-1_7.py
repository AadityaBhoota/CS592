def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    result = []
    group = ""
    stack = 0

    for char in paren_string:
        if char == '(':
            stack += 1
        group += char

        if stack == 0:
            result.append(group)
            group = ""

        if char == ')':
            stack -= 1

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