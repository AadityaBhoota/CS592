def max_Abs_Diff(arr, n):
    if len(arr) < 2:
        return 0
    
    max_diff = abs(arr[0] - arr[1])
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            max_diff = max(max_diff, abs(arr[i] - arr[j]))
    
    return max_diff

# Test the function with the provided examples




def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)