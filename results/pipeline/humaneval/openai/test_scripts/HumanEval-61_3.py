def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append('(')
        elif bracket == ')' and len(stack) == 0:
            return False
        elif bracket == ')' and len(stack) > 0:
            stack.pop()
    
    return len(stack) == 0



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