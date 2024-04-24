from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        result.append(max_depth)
    return result

# Test the function




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)