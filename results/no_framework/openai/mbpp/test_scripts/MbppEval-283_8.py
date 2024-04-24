def validate(n): 
    digit_count = [0] * 10
    n_str = str(n)
    
    for digit in n_str: 
        digit = int(digit)
        digit_count[digit] += 1
        if digit_count[digit] > digit: 
            return False
    
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)