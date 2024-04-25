def first_Digit(n):
    n_str = str(n)
    first_digit = int(n_str[0])
    return first_digit

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)