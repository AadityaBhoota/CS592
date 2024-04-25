def is_Sub_Array(A, B, m, n):
    # Two pointers to traverse the lists A and B
    i = 0
    j = 0
    
    # Traverse both arrays
    while i < m and j < n:
        if A[i] == B[j]:
            j += 1
        i += 1
    
    # If all elements of B are found in A in order
    return j == n

# Test cases




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)