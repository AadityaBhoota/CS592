from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_groups = paren_string.split()
    max_nesting_levels = []
    for group in paren_groups:
        max_nesting = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_nesting = max(max_nesting, current_level)
            elif char == ')':
                current_level -= 1
        max_nesting_levels.append(max_nesting)
    
    return max_nesting_levels



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]

check(parse_nested_parens)