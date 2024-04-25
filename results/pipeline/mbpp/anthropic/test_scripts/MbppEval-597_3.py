def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while k > 1:
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        else:
            if i < len(arr1):
                i += 1
            else:
                j += 1
        k -= 1
    
    if i < len(arr1) and j < len(arr2):
        return min(arr1[i], arr2[j])
    elif i < len(arr1):
        return arr1[i]
    else:
        return arr2[j]

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)