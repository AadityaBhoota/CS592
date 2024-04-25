def is_undulating(n):
    n = str(n)
    if len(n) < 3:
        return False
    
    for i in range(2, len(n)):
        if n[i-2] == n[i-1] or n[i-1] == n[i]:
            return False
    return True

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)