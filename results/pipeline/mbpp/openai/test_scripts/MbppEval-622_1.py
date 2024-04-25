def merge_sorted_lists(arr1, arr2):
    merged = []
    
    i, j = 0, 0
    
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

def get_median(arr1, arr2, n):
    merged_list = merge_sorted_lists(arr1, arr2)
    middle_index = n // 2 if n % 2 != 0 else (n // 2) - 1

    if n % 2 != 0:
        return float(merged_list[middle_index])
    else:
        return (merged_list[middle_index] + merged_list[middle_index - 1]) / 2

# Test the get_median function
arr1 = [3, 6, 14, 23, 36, 42]
arr2 = [2, 18, 27, 39, 49, 55]
median = get_median(arr1, arr2, 6)


def check(candidate):
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

check(get_median)