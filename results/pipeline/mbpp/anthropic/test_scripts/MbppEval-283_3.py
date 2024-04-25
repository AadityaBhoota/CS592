def validate(n):
    freq_dict = {}
    str_n = str(n)
    
    for char in str_n:
        digit = int(char)
        if digit not in freq_dict:
            freq_dict[digit] = 1
        else:
            freq_dict[digit] += 1
    
    for digit, count in freq_dict.items():
        if count > digit:
            return False
    
    return True

def check(candidate):
    assert validate(1234) == True
    assert validate(51241) == False
    assert validate(321) == True

check(validate)