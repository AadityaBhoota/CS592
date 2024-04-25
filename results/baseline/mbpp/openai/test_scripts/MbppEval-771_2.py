def check_expression(exp):
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    stack = []
    
    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    
    return len(stack) == 0

# Test cases




def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)