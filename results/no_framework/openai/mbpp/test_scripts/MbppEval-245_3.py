def max_sum(arr):
    n = len(arr)

    # Initialize two arrays to store the maximum increasing sum ending at each index and maximum decreasing sum starting at each index
    inc_sum = [0] * n
    dec_sum = [0] * n

    # Calculate the maximum increasing sum
    for i in range(n):
        inc_sum[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                inc_sum[i] = max(inc_sum[i], inc_sum[j] + arr[i])

    # Calculate the maximum decreasing sum
    for i in range(n - 1, -1, -1):
        dec_sum[i] = arr[i]
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                dec_sum[i] = max(dec_sum[i], dec_sum[j] + arr[i])

    # Find the maximum sum of bitonic subsequence
    max_bitonic_sum = float('-inf')
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, inc_sum[i] + dec_sum[i] - arr[i])

    return max_bitonic_sum

# Test the function with the provided examples




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)