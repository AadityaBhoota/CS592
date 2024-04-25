def is_undulating(n):
    digits = [int(d) for d in n]
    is_up = None
    trend_changes = 0
    prev_digit = None

    for i in range(1, len(digits)):
        if digits[i] > digits[i-1]:
            if is_up is False:
                trend_changes += 1
            is_up = True
        elif digits[i] < digits[i-1]:
            if is_up is True:
                trend_changes += 1
            is_up = False
        prev_digit = digits[i-1]

    return trend_changes == len(digits) - 1

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)