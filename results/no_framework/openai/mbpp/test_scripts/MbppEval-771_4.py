def check_expression(exp):
    stack = deque()
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in exp:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or stack.pop() != brackets_map[char]:
                return False

    return len(stack) == 0

# Test cases




def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)