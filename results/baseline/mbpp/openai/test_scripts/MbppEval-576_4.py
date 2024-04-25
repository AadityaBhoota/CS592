def is_Sub_Array(A, B, m, n):
    # Function to check whether list B is a sublist of list A
    # m = length of list A, n = length of list B
    i = 0
    j = 0

    while i < m and j < n:
        if A[i] == B[j]:
            j += 1
        else:
            j = 0
        
        i += 1

    return j == n


# Test cases




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)