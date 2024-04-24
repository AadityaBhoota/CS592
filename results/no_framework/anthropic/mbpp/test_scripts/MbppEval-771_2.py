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
    mapping = {")": "(", "}": "{", "]": "["}

    for char in exp:
        if char in mapping:
            # If the current character is a closing bracket,
            # check if the top element in the stack matches the closing bracket
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        else:
            # If the current character is an opening bracket,
            # push it onto the stack
            stack.append(char)

    # If the stack is empty, it means the expression is balanced
    return len(stack) == 0

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)