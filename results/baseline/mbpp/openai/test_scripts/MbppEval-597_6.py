def find_kth(arr1, arr2, k):
    if not arr1:
        return arr2[k]
    if not arr2:
        return arr1[k]

    mid1 = len(arr1) // 2
    mid2 = len(arr2) // 2

    if mid1 + mid2 < k:
        if arr1[mid1] > arr2[mid2]:
            return find_kth(arr1, arr2[mid2+1:], k - mid2 - 1)
        else:
            return find_kth(arr1[mid1+1:], arr2, k - mid1 - 1)
    else:
        if arr1[mid1] > arr2[mid2]:
            return find_kth(arr1[:mid1], arr2, k)
        else:
            return find_kth(arr1, arr2[:mid2], k)

# Test the function with the given examples




def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)