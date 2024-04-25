from collections import deque

def check_expression(exp):
    stack = deque()
    
    for char in exp:
        if char in ['{', '(', '[']:
            stack.append(char)
        elif char in ['}', ')', ']']:
            if not stack:
                return False
            top = stack.pop()
            if (char == '}' and top != '{' or 
                char == ')' and top != '(' or
                char == ']' and top != '['):
                return False
    
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)