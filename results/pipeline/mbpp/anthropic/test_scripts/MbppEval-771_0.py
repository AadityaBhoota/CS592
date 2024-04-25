from collections import deque

def check_expression(exp):
    bracket_map = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    stack = deque()

    for char in exp:
        if char in bracket_map:
            stack.append(char)
        elif char in bracket_map.values():
            if not stack:
                return False
            top = stack.pop()
            if bracket_map[top] != char:
                return False

    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)