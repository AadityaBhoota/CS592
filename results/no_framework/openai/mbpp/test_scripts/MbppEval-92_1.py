def is_undulating(n):
    n = str(n)
    
    if len(n) < 3:
        return False
    
    if all(x == n[0] for x in n[::2]) and all(y == n[1] for y in n[1::2]) and n[0] != n[1]:
        return True
    elif all(x == n[1] for x in n[::2]) and all(y == n[0] for y in n[1::2]) and n[0] != n[1]:
        return True
    else:
        return False

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)