def validate(n): 
    digits = str(n)
    freq = {}
    for digit in digits:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1

    for digit in digits:
        if freq[digit] > int(digit):
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)