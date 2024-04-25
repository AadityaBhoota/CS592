def correct_bracketing(brackets: str):
    opening_count = 0
    for bracket in brackets:
        if bracket == "<":
            opening_count += 1
        elif bracket == ">":
            opening_count -= 1
        if opening_count < 0:
            return False
    
    return opening_count == 0



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