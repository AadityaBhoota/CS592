def is_undulating(n): 
    n_str = str(n)
    if len(n_str) < 3:
        return False
    
    if n_str[0] == n_str[1]:
        return False
    
    for i in range(2, len(n_str)):
        if i % 2 == 0:
            if n_str[i] != n_str[0]:
                return False
        else:
            if n_str[i] != n_str[1]:
                return False

    return True

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)