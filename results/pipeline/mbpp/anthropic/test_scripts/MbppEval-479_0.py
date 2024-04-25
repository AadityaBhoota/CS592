def first_Digit(n):
    num_str = str(n)
    first_digit = int(num_str[0])
    return first_digit

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)