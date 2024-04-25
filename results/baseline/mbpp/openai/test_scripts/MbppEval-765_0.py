def is_polite(n):
    # Get the log base 2 of n
    power = math.log2(n+1)
    
    # Find the nth polite number using the formula
    polite_number = 2**(math.ceil(power))
    
    return polite_number

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)