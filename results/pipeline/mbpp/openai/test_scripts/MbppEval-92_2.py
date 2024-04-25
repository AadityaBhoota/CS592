def is_undulating(n):
    if len(n) < 3:
        return False
    
    if not n.isdigit():
        return False
    
    if n[0] == n[1]:
        return False

    for i in range(2, len(n)):
        if n[i] == n[i - 1] or n[i] != n[i - 2]:
            return False
    
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)