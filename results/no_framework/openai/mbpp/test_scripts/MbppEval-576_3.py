def is_Sub_Array(A, B):
    '''
    Write a Python function to check whether a list is a sublist of another or not.

    Examples:
    is_Sub_Array([1,4,3,5],[1,2]) == False
    is_Sub_Array([1,2,1],[1,2,1]) == True
    is_Sub_Array([1,0,2,2],[2,2,0]) == False
    '''
    for i in range(len(A) - len(B) + 1):
        if A[i:i+len(B)] == B:
            return True
    return False

# Test cases




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)