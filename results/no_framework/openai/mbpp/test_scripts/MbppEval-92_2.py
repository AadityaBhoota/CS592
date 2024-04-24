def is_undulating(n): 
    n = str(n)
    if len(n) < 3:
        return False
    
    pattern1 = n[0] + n[1] + n[0]
    pattern2 = n[1] + n[2] + n[1]
    
    for i in range(0, len(n)-5):
        if n[i:i+3] == pattern1 and n[i+3:i+6] == pattern2:
            return True
    return False

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)