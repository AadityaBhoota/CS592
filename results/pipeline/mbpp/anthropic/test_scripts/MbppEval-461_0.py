def upper_ctr(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)