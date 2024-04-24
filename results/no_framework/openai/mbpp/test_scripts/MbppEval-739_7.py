import math

def find_Index(n):
    '''
    Find the index of the smallest triangular number with n digits.
    
    Args:
        n: int, number of digits
        
    Returns:
        int, index of the smallest triangular number with n digits
    '''
    
    idx = 1
    while True:
        triangular_number = idx * (idx + 1) // 2
        num_digits = int(math.log10(triangular_number)) + 1
        if num_digits == n:
            return idx
        idx += 1

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)