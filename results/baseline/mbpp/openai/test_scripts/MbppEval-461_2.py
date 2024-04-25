def upper_ctr(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count

# Test the function




def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)