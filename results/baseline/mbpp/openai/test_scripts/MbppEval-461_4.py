def upper_ctr(s):
    return sum(1 for c in s if c.isupper())

# Test the function with the given examples
assert upper_ctr('PYthon') == 1
assert upper_ctr('BigData') == 1
assert upper_ctr('program') == 0

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)