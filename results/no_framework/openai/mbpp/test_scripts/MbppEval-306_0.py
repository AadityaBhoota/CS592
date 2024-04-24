def max_sum_increasing_subseq(arr, n, index, k):
    if k <= index:
        return sum(arr[:index+1])

    dp = [0] * n
    dp[index] = arr[index]

    for i in range(index + 1, n):
        if i == k:
            dp[i] = dp[index] + arr[i]
        else:
            dp[i] = arr[i]
            for j in range(index, i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])

    return max(dp)

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)