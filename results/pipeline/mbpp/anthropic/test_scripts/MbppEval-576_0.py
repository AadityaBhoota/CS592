def is_Sub_Array(A, B):
    i = 0
    j = 0
    
    for _ in range(len(A)):
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == len(B):
                return True
        else:
            i += 1
    
    return False

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)