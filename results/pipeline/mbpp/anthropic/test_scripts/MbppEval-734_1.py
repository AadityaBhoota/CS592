def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    total_sum = 0

    for i in range(n):
        dp[i][i] = arr[i]
        total_sum += dp[i][i]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = dp[i][j-1] * arr[j]
            total_sum += dp[i][j]

    return total_sum

def check(candidate):
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2]) == 5
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

check(sum_Of_Subarray_Prod)