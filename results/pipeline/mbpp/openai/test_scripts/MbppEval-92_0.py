def is_undulating(n): 
    if len(n) < 3:
        return False
    
    for i in range(2, len(n)):
        if (int(n[i]) - int(n[i-1])) * (int(n[i-1]) - int(n[i-2])) >= 0:
            return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)