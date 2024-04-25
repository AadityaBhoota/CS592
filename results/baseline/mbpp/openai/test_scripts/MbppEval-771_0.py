def check_expression(exp):
    stack = deque()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)