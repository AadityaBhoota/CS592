def correct_bracketing(brackets: str) -> bool:
    count = 0
    for bracket in brackets:
        if bracket == "(":
            count += 1
        elif bracket == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0

# Test cases
print(correct_bracketing("("))      # False
print(correct_bracketing("()"))     # True
print(correct_bracketing("(()())")) # True
print(correct_bracketing(")(()"))   # False



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