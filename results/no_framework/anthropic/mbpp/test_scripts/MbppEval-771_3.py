from collections import deque

def check_expression(exp):
    """
    Checks if the given expression is balanced or not.
    
    Args:
        exp (str): The expression to be checked.
        
    Returns:
        bool: True if the expression is balanced, False otherwise.
    """
    stack = deque()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    for char in exp:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            opening = stack.pop()
            if brackets[opening] != char:
                return False
    
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)