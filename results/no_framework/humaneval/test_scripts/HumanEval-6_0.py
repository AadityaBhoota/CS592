from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    max_depth = 0
    depth = 0

    for char in paren_string:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
    
    result.append(max_depth)
    
    return result

# Test the function with the provided example
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