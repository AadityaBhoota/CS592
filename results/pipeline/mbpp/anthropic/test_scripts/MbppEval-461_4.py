def upper_ctr(str):
    upper_count = 0
    for char in str:
        if char.isupper():
            upper_count += 1
    return upper_count

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)