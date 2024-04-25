def correct_bracketing(brackets: str):
    open_brackets = 0
    for char in brackets:
        if char == "<":
            open_brackets += 1
        elif char == ">":
            if open_brackets == 0:
                return False
            open_brackets -= 1
    return open_brackets == 0



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