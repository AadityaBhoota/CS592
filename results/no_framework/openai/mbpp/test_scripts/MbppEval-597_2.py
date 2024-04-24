def find_kth(arr1, arr2, k):
    len1 = len(arr1)
    len2 = len(arr2)
    
    if len1 > len2:
        return find_kth(arr2, arr1, k)
    
    if len1 == 0:
        return arr2[k-1]
    
    if k == 1:
        return min(arr1[0], arr2[0])
    
    part_A = min(k//2, len1)
    part_B = k - part_A
    
    if arr1[part_A - 1] < arr2[part_B - 1]:
        return find_kth(arr1[part_A:], arr2, k - part_A)
    else:
        return find_kth(arr1, arr2[part_B:], k - part_B)

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)