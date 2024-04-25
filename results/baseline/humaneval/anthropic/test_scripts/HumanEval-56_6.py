def correct_bracketing(brackets: str):
    """
    Checks if every opening bracket has a corresponding closing bracket.

    Args:
        brackets (str): A string of "<" and ">" characters.

    Returns:
        bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    """
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        elif char == ">":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0



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