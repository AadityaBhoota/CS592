def is_Diff(n):
    '''
    Function to find whether a number is divisible by 11.
    
    Arguments:
    n : int - The number to check
    
    Returns:
    bool : True if divisible by 11, False otherwise
    '''
    odd_sum = 0
    even_sum = 0
    n = str(n)

    for i, digit in enumerate(n):
        if i % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    
    diff = abs(odd_sum - even_sum)

    if diff % 11 == 0:
        return True
    else:
        return False

# Test cases




def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)