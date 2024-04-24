def upper_ctr(string):
    return sum(1 for char in string if char.isupper())

# Test cases




def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)