def correct_bracketing(brackets: str):
    opened = 0

    for bracket in brackets:
        if bracket == "<":
            opened += 1
        elif bracket == ">" and opened > 0:
            opened -= 1
        else:
            return False

    return opened == 0

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