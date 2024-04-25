from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()

    def max_nesting_level(parentheses: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in parentheses:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    return [max_nesting_level(group) for group in groups]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)