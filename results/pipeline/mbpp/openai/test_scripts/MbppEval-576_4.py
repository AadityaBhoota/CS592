def is_Sub_Array(A, B):
    if len(B) > len(A):
        return False

    for i in range(len(A)):
        if A[i:i+len(B)] == B:
            return True
    return False

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)