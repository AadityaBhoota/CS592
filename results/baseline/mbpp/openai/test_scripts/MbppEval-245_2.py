def max_sum(arr):
    n = len(arr)
    max_increasing = [0] * n
    max_decreasing = [0] * n

    for i in range(n):
        max_increasing[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_increasing[i] = max(max_increasing[i], max_increasing[j] + arr[i])

    for i in range(n - 1, -1, -1):
        max_decreasing[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                max_decreasing[i] = max(max_decreasing[i], max_decreasing[j] + arr[i])

    max_bitonic = 0
    for i in range(n):
        max_bitonic = max(max_bitonic, max_increasing[i] + max_decreasing[i] - arr[i])

    return max_bitonic

# Test cases




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)