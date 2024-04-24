def is_Sub_Array(A, B, len_A, len_B):
    """
    Checks whether a list B is a sublist of another list A.

    Args:
        A (list): The main list.
        B (list): The sublist to check.
        len_A (int): The length of list A.
        len_B (int): The length of list B.

    Returns:
        bool: True if B is a sublist of A, False otherwise.
    """
    if len_B > len_A:
        return False

    for i in range(len_A - len_B + 1):
        if A[i:i+len_B] == B:
            return True

    return False

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)