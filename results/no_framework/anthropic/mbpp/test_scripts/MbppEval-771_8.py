from collections import deque

def check_expression(exp):
    """
    Write a function to check if the given expression is balanced or not.
    
    Examples:
    check_expression("{()}[{}]") == True
    check_expression("{()}[{]") == False
    check_expression("{()}[{}][]({})") == True
    """
    stack = deque()
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in exp:
        if char in match.values():
            stack.append(char)
        elif char in match.keys():
            if not stack or match[char] != stack.pop():
                return False
    
    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)