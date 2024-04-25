def validate(n):
    str_n = str(n)
    digit_count = {}

    for digit in str_n:
        digit_count[digit] = digit_count.get(digit, 0) + 1

    for digit, count in digit_count.items():
        if count > int(digit):
            return False

    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)