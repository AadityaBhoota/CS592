from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    curr_depth = 0
    max_depth = 0

    for char in paren_string:
        if char == '(':
            curr_depth += 1
            max_depth = max(max_depth, curr_depth)
        elif char == ')':
            curr_depth -= 1

    return depths

# Test the function
result = parse_nested_parens('(()()) ((())) () ((())()())')




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)