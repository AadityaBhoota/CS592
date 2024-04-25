def is_nonagonal(n):
    if n < 1:
        return None
    nonagonal_num = n * (7*n - 5) // 2
    
    return nonagonal_num

# Test cases




def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)