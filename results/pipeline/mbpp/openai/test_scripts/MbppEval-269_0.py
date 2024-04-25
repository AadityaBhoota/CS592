def ascii_value(k):
    if isinstance(k, str) and len(k) == 1:
        ascii_val = ord(k)
        return ascii_val
    else:
        return "Input should be a single character."

def check(candidate):
    assert ascii_value('A')==65
    assert ascii_value('R')==82
    assert ascii_value('S')==83

check(ascii_value)