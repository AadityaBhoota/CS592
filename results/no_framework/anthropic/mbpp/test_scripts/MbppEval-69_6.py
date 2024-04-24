def is_sublist(l, s):
    """
    Check whether a list contains the given sublist or not.

    Args:
        l (list): The main list.
        s (list): The sublist to be checked.

    Returns:
        bool: True if the sublist is present in the main list, False otherwise.
    """
    for i in range(len(l) - len(s) + 1):
        if l[i:i+len(s)] == s:
            return True
    return False

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False

check(is_sublist)