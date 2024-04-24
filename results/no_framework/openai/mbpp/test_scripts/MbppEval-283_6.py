def validate(n): 
    digits = [int(d) for d in str(n)]
    for digit in digits:
        if digits.count(digit) > digit:
            return False
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)