def is_octagonal(n): 
    return n * (3 * n - 2)

# Test the function with the given examples




def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)