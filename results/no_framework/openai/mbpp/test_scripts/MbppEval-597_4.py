def find_kth(arr1, arr2, k):
    # If one of the lists is empty, return kth element from the other list
    if not arr1:
        return arr2[k-1]
    if not arr2:
        return arr1[k-1]
    
    # If k becomes 1, return the minimum of the first elements of both lists
    if k == 1:
        return min(arr1[0], arr2[0])
    
    # Calculate mid indices
    mid1 = min(k // 2, len(arr1))
    mid2 = k - mid1
    
    # Compare the mid elements of both lists
    if arr1[mid1 - 1] < arr2[mid2 - 1]:
        return find_kth(arr1[mid1:], arr2, k - mid1)
    else:
        return find_kth(arr1, arr2[mid2:], k - mid2)

# Test the function with example inputs




def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)