def find_kth(arr1, arr2, k):
    total_len = len(arr1) + len(arr2)
    if k > total_len:
        return None

    if not arr1:
        return arr2[k-1]
    if not arr2:
        return arr1[k-1]

    idx1, idx2 = 0, 0
    kth_element = None

    while idx1 + idx2 < k:
        if idx1 == len(arr1):
            kth_element = arr2[idx2]
            idx2 += 1
        elif idx2 == len(arr2):
            kth_element = arr1[idx1]
            idx1 += 1
        elif arr1[idx1] < arr2[idx2]:
            kth_element = arr1[idx1]
            idx1 += 1
        else:
            kth_element = arr2[idx2]
            idx2 += 1

    return kth_element

# Test the function with provided examples




def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)