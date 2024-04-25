from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    output = []
    for group in paren_string.split():
        max_nesting = 0
        current_nesting = 0
        for char in group:
            if char == '(':
                current_nesting += 1
                max_nesting = max(max_nesting, current_nesting)
            elif char == ')':
                current_nesting -= 1
        output.append(max_nesting)
    return output



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)