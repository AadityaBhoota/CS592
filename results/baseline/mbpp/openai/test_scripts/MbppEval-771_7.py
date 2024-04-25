def check_expression(exp):
    stack = deque()
    mapping = {"]": "[", "}": "{", ")": "("}
    
    for char in exp:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
                
    return not stack

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True

check(check_expression)