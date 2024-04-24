def is_octagonal(n): 
    if n < 1:
        return "Input should be greater than or equal to 1"
    
    return n * (3 * n - 2)

# Test cases




def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)