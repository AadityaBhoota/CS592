def ascii_value(k):
    return ord(k)

def check(candidate):
    assert ascii_value('A')==65
    assert ascii_value('R')==82
    assert ascii_value('S')==83

check(ascii_value)