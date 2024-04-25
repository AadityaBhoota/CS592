def is_nonagonal(n):
    return n * (7 * n - 5) // 2

# Testing the function with the examples provided




def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)