def number_ctr(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

# Test cases




def check(candidate):
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') == 1
    assert number_ctr('123') == 3
    assert number_ctr('3wond-1ers2') == 3

check(number_ctr)