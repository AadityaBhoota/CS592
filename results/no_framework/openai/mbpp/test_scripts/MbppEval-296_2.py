def get_Inv_Count(arr):
    '''
    This function counts the number of inversions in an array.

    An inversion in an array arr occurs when there are two indices i and j such that i < j and arr[i] > arr[j].

    Parameters:
    arr (list): The input array for which inversions need to be counted.

    Returns:
    count (int): The number of inversions in the input array.
    '''
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

# Test cases



def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)