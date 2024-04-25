from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
            max_depth = max(max_depth, len(stack))
        result.append(max_depth)
    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)