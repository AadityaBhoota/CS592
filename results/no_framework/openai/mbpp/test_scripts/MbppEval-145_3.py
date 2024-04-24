def max_Abs_Diff(arr, n):
    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

# Test cases




def check(candidate):
    assert max_Abs_Diff((2,1,5,3)) == 4
    assert max_Abs_Diff((9,3,2,5,1)) == 8
    assert max_Abs_Diff((3,2,1)) == 2

check(max_Abs_Diff)