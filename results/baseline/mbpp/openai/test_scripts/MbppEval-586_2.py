def split_Arr(arr, n):
    '''
    Split a list at the nth element and add the first part to the end.
    
    Args:
    arr: List to be splitted and rotated.
    n: Index at which to split the list.
    
    Returns:
    List after splitting and rotating.
    '''
    if n >= len(arr):
        return arr
    else:
        return arr[n:] + arr[:n]

# Examples provided in the function's docstring




def check(candidate):
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

check(split_Arr)