def max_Abs_Diff(arr, n):
    if len(arr) < 2:
        return None
    
    min_val, max_val = min(arr), max(arr)
    min_count = arr.count(min_val)
    max_count = arr.count(max_val)
    
    if min_count == len(arr) or max_count == len(arr):
        return 0
    
    return max(abs(max_val - min_val), n - 1)

# Test cases




def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)