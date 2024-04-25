def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0

# Testing the function
if __name__ == "__main__":
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False

    print("All tests passed!")



METADATA = {}


def check(candidate):
    assert candidate("()")
    assert candidate("(()())")
    assert candidate("()()(()())()")
    assert candidate("()()((()()())())(()()(()))")
    assert not candidate("((()())))")
    assert not candidate(")(()")
    assert not candidate("(")
    assert not candidate("((((")
    assert not candidate(")")
    assert not candidate("(()")
    assert not candidate("()()(()())())(()")
    assert not candidate("()()(()())()))()")


check(correct_bracketing)