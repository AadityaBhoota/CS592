def ascii_value(k):
    """
    Write a function to find the ascii value of a character.

    Examples:
    ascii_value('A') == 65
    ascii_value('R') == 82
    ascii_value('S') == 83
    """
    if isinstance(k, str) and len(k) == 1:
        return ord(k)
    else:
        return None

def check(candidate):
    assert ascii_value('A')==65
    assert ascii_value('R')==82
    assert ascii_value('S')==83

check(ascii_value)