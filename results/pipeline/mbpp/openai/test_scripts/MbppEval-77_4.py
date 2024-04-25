def is_Diff(n): 
    if n % 11 == 0:
        return True
    else:
        return False

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)