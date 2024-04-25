def is_octagonal(n):
    # input: n (integer)
    
    # Calculate the nth octagonal number using the formula: n(3n-1)(2n+1)
    octagonal_number = n * (3*n - 1) * (2*n + 1)

    return octagonal_number

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)