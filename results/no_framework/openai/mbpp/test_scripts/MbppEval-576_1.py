def is_Sub_Array(A, B):
    """
    Check whether a list is a sublist of another or not.

    Args:
    A: list, the main list to check against
    B: list, the sublist to check

    Returns:
    bool: True if B is a sublist of A, otherwise False

    Examples:
    is_Sub_Array([1, 4, 3, 5], [1, 2]) -> False
    is_Sub_Array([1, 2, 1], [1 ,2, 1]) -> True
    is_Sub_Array([1, 0, 2, 2], [2, 2, 0]) -> False
    """
    if not B:
        return True
    if not A:
        return False

    for i in range(len(A)):
        if A[i] == B[0]:
            if A[i:i+len(B)] == B:
                return True

    return False

# Testing the function with the provided examples




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)