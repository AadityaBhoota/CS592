from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    res = []
    max_nesting_level = 0
    current_nesting_level = 0

    for char in paren_string:
        if char == '(':
            current_nesting_level += 1
            max_nesting_level = max(max_nesting_level, current_nesting_level)
        elif char == ')':
            current_nesting_level -= 1

    res.append(max_nesting_level)

    return res

# Test the function
result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)