def is_nonagonal(n):
    if n <= 0:
        return "Input should be a positive integer"
    return n * (7*n - 5) // 2

# Test cases




def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)