from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    max_depth = 0
    current_depth = 0

    for char in paren_string:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return [max_depth]


# Test the function with sample input
input_string = '(()()) ((())) () ((())()())'
output = parse_nested_parens(input_string)




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)