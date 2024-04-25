def is_num_decagonal(n): 
    if n <= 0:
        return "Input must be a positive integer."
    else:
        return n * (7 * n - 5)

# Test the function with the given examples




def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370

check(is_num_decagonal)