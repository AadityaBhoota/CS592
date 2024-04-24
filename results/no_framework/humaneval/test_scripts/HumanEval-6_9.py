from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    max_depth = 0
    depth = 0

    for char in paren_string:
        if char == "(":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif char == ")":
            depth -= 1

    return [max_depth]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [3]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)