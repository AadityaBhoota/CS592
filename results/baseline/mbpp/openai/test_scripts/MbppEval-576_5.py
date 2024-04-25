def is_Sub_Array(A, B, m, n): 
    '''
    Check whether a list is sublist of another list or not.
    
    Arguments:
    A -- The main list
    B -- The sublist to be checked
    m -- Length of main list A
    n -- Length of sublist B
    
    Returns:
    result -- True if B is a sublist of A, otherwise False
    '''
    if n == 0: 
        return True

    if m == 0: 
        return False

    if A[m-1] == B[n-1]: 
        return is_Sub_Array(A, B, m-1, n-1) 

    return is_Sub_Array(A, B, m-1, n) 

# Examples




def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    assert is_Sub_Array([1,2,1],[1,2,1]) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

check(is_Sub_Array)