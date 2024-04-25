def is_nonagonal(n):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer."
    
    nonagonal_number = n * (7*n - 5) // 2
    return nonagonal_number

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)