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
    pairs = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    for char in exp:
        if char in pairs:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if pairs[top] != char:
                    return False
            else:
                return False

    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)