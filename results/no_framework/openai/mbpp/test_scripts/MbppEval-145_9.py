def max_Abs_Diff(arr, n):
    arr.sort()
    return abs(arr[0] - arr[n-1])

# Test cases




def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)