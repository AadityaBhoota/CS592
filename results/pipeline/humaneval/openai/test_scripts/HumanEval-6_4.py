from typing import List


def max_nesting_level(group: str) -> int:
    max_depth = 0
    depth = 0

    for char in group:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1

    return max_depth


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    nesting_levels = [max_nesting_level(group) for group in groups]
    return nesting_levels



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)