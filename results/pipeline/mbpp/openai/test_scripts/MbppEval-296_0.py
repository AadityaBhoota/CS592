def get_Inv_Count(arr):
    count = 0
    
    def merge(arr1, arr2):
        nonlocal count
        i = j = 0
        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                count += len(arr1) - i
                j += 1
        merged += arr1[i:]
        merged += arr2[j:]
        return merged

    def sort_and_count(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort_and_count(arr[:mid])
        right = sort_and_count(arr[mid:])
        return merge(left, right)

    sort_and_count(arr)

    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)