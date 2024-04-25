def get_Inv_Count(arr):
    count = 0

    def merge_sort_and_count_inversions(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, inv_count_left = merge_sort_and_count_inversions(arr[:mid])
        right, inv_count_right = merge_sort_and_count_inversions(arr[mid:])
        
        inv_count_merge = 0
        sorted_arr = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                inv_count_merge += len(left) - i
                count += len(left) - i

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr, inv_count_left + inv_count_right + inv_count_merge

    sorted_arr, _ = merge_sort_and_count_inversions(arr)
    
    return count

def check(candidate):
    assert get_Inv_Count([1,20,6,4,5]) == 5
    assert get_Inv_Count([1,2,1]) == 1
    assert get_Inv_Count([1,2,5,6,1]) == 3

check(get_Inv_Count)