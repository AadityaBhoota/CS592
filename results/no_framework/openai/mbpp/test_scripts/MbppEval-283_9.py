def validate(n):
    digit_count = [0] * 10

    for digit in str(n):
        digit_count[int(digit)] += 1

    for i in range(1, 10):
        if digit_count[i] > i:
            return False

    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)