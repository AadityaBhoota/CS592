def is_Diff(n): 
    return (sum(int(digit) if idx % 2 == 0 else -int(digit) for idx, digit in enumerate(str(n))) % 11 == 0)

# Test cases




def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)