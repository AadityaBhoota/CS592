def validate(n):
    num_str = str(n)
    for digit in num_str:
        if num_str.count(digit) > int(digit):
            return False
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)