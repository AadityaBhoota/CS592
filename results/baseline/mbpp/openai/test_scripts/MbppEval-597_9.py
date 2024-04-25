def find_kth(arr1, arr2, k):
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
        else:
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1

    while i < len(arr1):
        k -= 1
        if k == 0:
            return arr1[i]
        i += 1

    while j < len(arr2):
        k -= 1
        if k == 0:
            return arr2[j]
        j += 1

# Test cases




def check(candidate):
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

check(find_kth)