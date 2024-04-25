def max_Abs_Diff(arr):
    max_diff = None
    min_val = None
    
    for num in arr:
        if min_val is None or num < min_val:
            min_val = num
    
    max_diff = None

    for num in arr:
        if min_val is None or num < min_val:
            min_val = num
        if max_diff is None or abs(num - min_val) > max_diff:
            max_diff = abs(num - min_val)

    return max_diff

def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)