def is_octagonal(n):
    octagonal_number = 2 * n**2 - n
    return octagonal_number

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)