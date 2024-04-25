def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    max_depth = 0
    cur_depth = 0

    for char in paren_string:
        if char == '(':
            cur_depth += 1
            max_depth = max(max_depth, cur_depth)
        elif char == ')':
            cur_depth -= 1

    return result

# Test the function with sample input
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