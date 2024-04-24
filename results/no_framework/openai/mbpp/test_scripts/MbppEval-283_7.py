def validate(n): 
    n_str = str(n)
    freq = {}
    
    for digit in n_str:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
    
    for digit, count in freq.items():
        if int(digit) < count:
            return False
    
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)