def is_undulating(n):
    n = str(n)
    
    if len(n) < 3:
        return False
    
    if n[0] == n[2]:
        for i in range(3, len(n), 2):
            if n[i] != n[0]:
                return False
    else:
        for i in range(3, len(n), 2):
            if n[i] != n[1]:
                return False
        
    return True

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)