def check_Consecutive(l):
    """
    Write a python function to check whether the given list contains consecutive numbers or not.

    Examples:
    check_Consecutive([1,2,3,4,5]) == True
    check_Consecutive([1,2,3,5,6]) == False
    check_Consecutive([1,2,1]) == False
    """
    is_consecutive = True
    for i in range(len(l) - 1):
        if l[i+1] - l[i] != 1:
            is_consecutive = False
            break
    return is_consecutive

def check(candidate):
    assert check_Consecutive([1,2,3,4,5]) == True
    assert check_Consecutive([1,2,3,5,6]) == False
    assert check_Consecutive([1,2,1]) == False

check(check_Consecutive)