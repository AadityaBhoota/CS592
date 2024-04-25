from collections import deque

def check_expression(exp):
    """
    Check if the given expression is balanced or not.
    
    Args:
        exp (str): The expression to be checked.
    
    Returns:
        bool: True if the expression is balanced, False otherwise.
    """
    # Define a dictionary to map opening brackets to their corresponding closing brackets
    bracket_map = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    
    # Create a stack to keep track of the opening brackets
    stack = deque()
    
    for char in exp:
        if char in bracket_map:
            # If the current character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_map.values():
            # If the current character is a closing bracket
            if not stack:
                # If the stack is empty, the expression is unbalanced
                return False
            
            # Pop the last opening bracket from the stack and check if it matches the current closing bracket
            last_opening = stack.pop()
            if bracket_map[last_opening] != char:
                return False
    
    # If the stack is empty, the expression is balanced
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)