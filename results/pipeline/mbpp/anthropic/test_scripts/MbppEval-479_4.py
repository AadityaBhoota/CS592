def first_Digit(n):
    num_str = str(n)
    return int(num_str[0])

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)