def is_num_decagonal(n):
    if n < 1:
        return "Invalid input. Please enter a positive integer."
    
    # Formula for nth decagonal number: Dn = n(7n - 5)
    decagonal_num = n*(7*n - 5)
    
    return decagonal_num

# Test cases




def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370

check(is_num_decagonal)