def is_undulating(n):
    # Check if the length of the number is less than 3
    if len(n) < 3:
        return False
    
    # Check if the number is undulating or not
    for i in range(2, len(n)):
        if n[i] == n[i-2]:
            return False
    return True

# Test cases




def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)