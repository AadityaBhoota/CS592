def correct_bracketing(brackets: str):
    stack = []

    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">" and stack:
            stack.pop()
        else:
            return False

    return len(stack) == 0

# Test cases







METADATA = {}


def check(candidate):
    assert candidate("<>")
    assert candidate("<<><>>")
    assert candidate("<><><<><>><>")
    assert candidate("<><><<<><><>><>><<><><<>>>")
    assert not candidate("<<<><>>>>")
    assert not candidate("><<>")
    assert not candidate("<")
    assert not candidate("<<<<")
    assert not candidate(">")
    assert not candidate("<<>")
    assert not candidate("<><><<><>><>><<>")
    assert not candidate("<><><<><>><>>><>")


check(correct_bracketing)