def get_Inv_Count(arr, n):
    """
    Counts the number of inversions in the given array.
    
    Args:
        arr (list): The input array.
        n (int): The length of the input array.
        
    Returns:
        int: The number of inversions in the array.
    """
    return merge_sort(arr, 0, n - 1)

def merge_sort(arr, left, right):
    """
    Implements the merge sort algorithm to count the number of inversions.
    
    Args:
        arr (list): The input array.
        left (int): The left index of the subarray.
        right (int): The right index of the subarray.
        
    Returns:
        int: The number of inversions in the subarray.
    """
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    
    # Count inversions in the left and right subarrays
    left_count = merge_sort(arr, left, mid)
    right_count = merge_sort(arr, mid + 1, right)
    
    # Merge the subarrays and count the inversions
    return left_count + right_count + merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays and counts the number of inversions.
    
    Args:
        arr (list): The input array.
        left (int): The left index of the first subarray.
        mid (int): The middle index of the first subarray.
        right (int): The right index of the second subarray.
        
    Returns:
        int: The number of inversions between the two subarrays.
    """
    i, j = left, mid + 1
    count = 0
    
    # Create a temporary array to store the merged elements
    temp = [0] * (right - left + 1)
    k = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1
            j += 1
        k += 1
    
    # Add remaining elements from the left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    # Add remaining elements from the right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Update the original array with the merged elements
    for i in range(left, right + 1):
        arr[i] = temp[i - left]
    
    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)