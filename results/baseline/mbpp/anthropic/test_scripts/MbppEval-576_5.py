def is_Sub_Array(A, B):
    """
    Checks whether a list B is a sublist of another list A.

    Args:
        A (list): The main list.
        B (list): The sublist to be checked.

    Returns:
        bool: True if B is a sublist of A, False otherwise.
    """
    n, m = len(A), len(B)
    if m > n:
        return False

    for i in range(n - m + 1):
        if A[i:i+m] == B:
            return True

    return False

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)