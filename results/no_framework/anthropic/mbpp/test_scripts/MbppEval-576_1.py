def is_Sub_Array(A, B, A_len, B_len):
    """
    Checks whether list B is a sublist of list A.

    Args:
        A (list): The main list.
        B (list): The sublist to be checked.
        A_len (int): The length of list A.
        B_len (int): The length of list B.

    Returns:
        bool: True if B is a sublist of A, False otherwise.
    """
    if B_len > A_len:
        return False

    for i in range(A_len - B_len + 1):
        if A[i:i+B_len] == B:
            return True

    return False

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)