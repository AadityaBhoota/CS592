def number_ctr(input_str):
    digit_count = 0
    for char in input_str:
        if char.isdigit():
            digit_count += 1
    return digit_count

def check(candidate):
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') == 1
    assert number_ctr('123') == 3
    assert number_ctr('3wond-1ers2') == 3

check(number_ctr)