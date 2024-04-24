def is_Even(n):
    '''
    Function to check whether the given number is even or not.
    
    Parameters:
    n (int): Input number to check for evenness.
    
    Returns:
    bool: True if the number is even, False otherwise.
    '''
    if n % 2 == 0:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False

check(is_Even)