def correct_bracketing(brackets: str):
    count = 0
    
    for bracket in brackets:
        if bracket == '<':
            count += 1
        elif bracket == '>':
            if count <= 0:
                return False
            count -= 1
    
    return count == 0



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