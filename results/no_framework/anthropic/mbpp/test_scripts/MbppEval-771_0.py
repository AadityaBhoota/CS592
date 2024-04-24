from collections import deque

def check_expression(exp):
    """
    Write a function to check if the given expression is balanced or not.
    """
    stack = deque()
    opening_brackets = "{[("
    closing_brackets = "}])"
    bracket_pairs = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top_bracket = stack.pop()
            if bracket_pairs[top_bracket] != char:
                return False

    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)