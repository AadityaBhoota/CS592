def is_Sub_Array(A,B,m,n): 
    # If B is an empty list, it is always a sublist of A
    if n == 0:
        return True

    # If B is not empty but A is empty, B can't be a sublist of A
    if m == 0:
        return False

    # Traverse both arrays with two pointers and try to match elements of B in A
    for i in range(m):
        # If the element in A matches the first element in B
        if A[i] == B[0]:
            # Initialize variables to track the matching sequence
            j = 0  # Pointer for B
            k = i  # Pointer for A
            
            # Check if the current elements in A and B match
            while j < n and k < m and A[k] == B[j]:
                j += 1
                k += 1
            
            # If all elements in B are matched in A, return True
            if j == n:
                return True

    # If no match is found, return False
    return False

# Test the function with the provided examples




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)