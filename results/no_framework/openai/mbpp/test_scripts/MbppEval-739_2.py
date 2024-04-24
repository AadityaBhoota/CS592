import math

def find_Index(n):
    '''
    This function finds the index of the smallest triangular number with n digits.
    
    Parameters:
    n (int): The number of digits
    
    Returns:
    index (int): The index of the smallest triangular number with n digits
    '''
    
    index = 1
    num_digits = 0
    triangular_num = 0

    # Loop until the number of digits of the triangular number is greater than or equal to n
    while num_digits < n:
        triangular_num += index
        num_digits = int(math.log10(triangular_num)) + 1
        index += 1

    return index - 1

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)