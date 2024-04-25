def get_median(arr1, arr2, n):
    merged = []
    i, j = 0, 0
    while i < n and j < n:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < n:
        merged.append(arr1[i])
        i += 1
    while j < n:
        merged.append(arr2[j])
        j += 1
    
    length = len(merged)
    if length % 2 == 0:
        return (merged[length // 2 - 1] + merged[length // 2]) / 2
    else:
        return merged[length // 2]

def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)