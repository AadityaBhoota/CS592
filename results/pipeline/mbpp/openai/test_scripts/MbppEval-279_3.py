def is_num_decagonal(n):
    if not isinstance(n, int) or n <= 0:
        return None

    decagonal_number = n * (7*n - 5)

    return decagonal_number

def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370

check(is_num_decagonal)