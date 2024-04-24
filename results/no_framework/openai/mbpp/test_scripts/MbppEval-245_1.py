def max_sum(arr):
    n = len(arr)

    # Initialize two arrays to store the maximum increasing sum and maximum decreasing sum ending at each index
    inc = [0] * n
    dec = [0] * n

    # Calculate the maximum increasing sum ending at each index
    for i in range(n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + arr[i])

    # Calculate the maximum decreasing sum starting at each index
    for i in range(n - 1, -1, -1):
        dec[i] = arr[i]
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    # Calculate the maximum sum of the bitonic subsequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

# Test the function with the provided examples




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)