def correct_bracketing(brackets: str):
    balance = 0
   
    for bracket in brackets:
        if bracket == "<":
            balance += 1
        elif bracket == ">":
            balance -= 1
            if balance < 0:
                return False

    return balance == 0



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