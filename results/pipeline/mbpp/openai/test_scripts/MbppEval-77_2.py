def is_Diff(n): 
    '''
    Write a python function to find whether a number is divisible by 11.

    Examples:
    is_Diff (12345) == False
    is_Diff(1212112) == True
    is_Diff(1212) == False
    '''
    return absolute_difference % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)