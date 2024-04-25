from collections import deque

def check_expression(exp):
    """
    Write a function to check if the given expression is balanced or not.
    """
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = deque()

    for char in exp:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)