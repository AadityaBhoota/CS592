def max_Abs_Diff(arr, n):
    arr.sort()
    return arr[n-1] - arr[0]

# Test the function with the provided examples




def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)