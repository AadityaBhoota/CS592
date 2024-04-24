def check_expression(exp):
    stack = deque()
    opening_brackets = ['{', '[', '(']
    closing_brackets = ['}', ']', ')']
    bracket_map = {']': '[', '}': '{', ')': '('}

    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return not stack

# Test cases




def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)