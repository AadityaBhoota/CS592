def correct_bracketing(brackets: str):
    opening_brackets = 0

    for bracket in brackets:
        if bracket == '<':
            opening_brackets += 1
        elif bracket == '>':
            opening_brackets -= 1
        
        if opening_brackets < 0:
            return False

    return opening_brackets == 0

# Testing the function with the given test cases
print(correct_bracketing("<"))    # Output: False
print(correct_bracketing("<>"))    # Output: True
print(correct_bracketing("<<><>>"))    # Output: True
print(correct_bracketing("><<>"))    # Output: False



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