def is_undulating(n):
    n = str(n)
    if len(n) < 3:
        return False

    prev_digit = n[0]
    same_count = 0

    for digit in n[1:]:
        if digit == prev_digit:
            same_count += 1
        else:
            if same_count != 1:
                return False
            same_count = 1

        prev_digit = digit

    return same_count == 1

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)