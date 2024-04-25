def is_undulating(n):
    if not isinstance(n, str):
        n = str(n)
    if not n:
        return False
    for i in range(len(n) - 1):
        if n[i] == n[i+1]:
            return False
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)