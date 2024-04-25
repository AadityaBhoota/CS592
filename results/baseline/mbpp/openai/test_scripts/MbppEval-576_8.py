def is_Sub_Array(A, B, m, n):
    '''
    Check whether a list is sublist of another or not.

    Examples:
    is_Sub_Array([1,4,3,5],[1,2],4,2) == False
    is_Sub_Array([1,2,1],[1,2,1],3,3) == True
    is_Sub_Array([1,0,2,2],[2,2,0],4,3) == False
    '''

    # Base Cases
    if n == 0:
        return True
    if m == 0:
        return False

    # If last elements of the lists match
    if A[m-1] == B[n-1]:
        return is_Sub_Array(A, B, m-1, n-1)

    # If last elements do not match
    return is_Sub_Array(A, B, m-1, n)

# Testing the function




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)