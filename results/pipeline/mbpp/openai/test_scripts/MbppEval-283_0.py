def validate(n):
    num_str = str(n)
    digit_count = {}
    
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    for digit, count in digit_count.items():
        if int(digit) < count:
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)