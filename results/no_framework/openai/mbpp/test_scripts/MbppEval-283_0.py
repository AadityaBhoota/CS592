def validate(n): 
    freq = {}
    for digit in str(n):
        freq[int(digit)] = freq.get(int(digit), 0) + 1
    for key, value in freq.items():
        if value > key:
            return False
    return True

# Test cases




def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)