from collections import deque

def check_expression(exp):
    stack = deque()
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in exp:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or bracket_map[char] != stack.pop():
                return False
    
    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)