from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    groups = paren_string.split()
    
    for group in groups:
        current_level = 0
        max_level = 0
        
        for char in group:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            
            max_level = max(max_level, current_level)
        
        result.append(max_level)
    
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