def is_octagonal(n):
    octagonal_num = n * (3 * n - 2)
    return octagonal_num

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)