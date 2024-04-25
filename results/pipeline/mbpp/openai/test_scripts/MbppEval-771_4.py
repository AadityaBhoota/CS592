from collections import deque

def check_expression(exp):
    stack = deque()
    
    for char in exp:
        if char in "([{":
            stack.append(char)
    
    for char in exp:
        if char in ")]}":
            if not stack:
                return False
            
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
    
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)