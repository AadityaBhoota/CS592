import math

def is_polite(n):
    """
    Find the nth polite number.
    """
    polite_numbers = [1]  # Start with the base case of 1
    i = 1
    while len(polite_numbers) < n:
        # Add the next power of 2
        polite_numbers.append(2 ** i)
        
        # Find all the possible sums of distinct powers of 2 less than or equal to the current power of 2
        for j in range(i):
            polite_numbers.append(2 ** j + 2 ** i)
        
        i += 1
    
    return polite_numbers[n-1]

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)