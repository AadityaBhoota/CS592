def check_expression(exp):
    stack = deque()
    open_brackets = set(['(', '{', '['])
    close_brackets = set([')', '}', ']'])
    bracket_pair = {')': '(', '}': '{', ']': '['}

    for char in exp:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or bracket_pair[char] != stack.pop():
                return False

    return len(stack) == 0

# Test cases




def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)