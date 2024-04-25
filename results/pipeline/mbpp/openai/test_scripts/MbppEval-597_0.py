def find_kth(arr1, arr2, k):
    '''
    Write a function to find kth element from the given two sorted arrays.

    Examples:
    find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5) == 6
    find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7) == 256
    find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 5, 4, 6) == 8
    '''
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)