def first_Digit(n):
    n_str = str(n)
    return int(n_str[0])

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)