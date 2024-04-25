def first_Digit(n):
    num_as_str = str(n)
    return num_as_str[0]

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)