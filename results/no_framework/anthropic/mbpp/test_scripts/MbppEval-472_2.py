def check_Consecutive(l):
    """
    Write a python function to check whether the given list contains consecutive numbers or not.

    Examples:
    check_Consecutive([1,2,3,4,5]) == True
    check_Consecutive([1,2,3,5,6]) == False
    check_Consecutive([1,2,1]) == False
    """
    if len(l) < 2:
        return False
    
    for i in range(1, len(l)):
        if l[i] - l[i-1] != 1:
            return False
    
    return True

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)