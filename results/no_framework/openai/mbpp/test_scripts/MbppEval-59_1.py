def is_octagonal(n):
    if n <= 0:
        return "Input must be a positive integer."

    return n * (3*n - 2)

# Test cases




def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)