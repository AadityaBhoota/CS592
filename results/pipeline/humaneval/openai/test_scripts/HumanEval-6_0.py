from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    
    for group in groups:
        max_count = 0
        open_count = 0
        
        for char in group:
            if char == '(':
                open_count += 1
                if open_count > max_count:
                    max_count = open_count
            elif char == ')':
                open_count -= 1
        
        result.append(max_count)
    
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