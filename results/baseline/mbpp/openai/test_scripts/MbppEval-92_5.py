def is_undulating(n): 
    n = str(n)
    if len(set(n)) != 2:
        return False

    return all(n[i] != n[i+1] for i in range(len(n)-1))

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)