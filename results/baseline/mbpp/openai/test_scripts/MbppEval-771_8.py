def check_expression(exp):
    stack = deque()
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in exp:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack

# Test cases




def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)