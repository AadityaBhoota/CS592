def max_sum(arr):
    n = len(arr)

    increasing = [0] * n
    decreasing = [0] * n

    for i in range(n):
        increasing[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                increasing[i] = max(increasing[i], increasing[j] + arr[i])

    for i in range(n - 1, -1, -1):
        decreasing[i] = arr[i]
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                decreasing[i] = max(decreasing[i], decreasing[j] + arr[i])

    max_sum_bitonic = 0
    for i in range(n):
        max_sum_bitonic = max(max_sum_bitonic, increasing[i] + decreasing[i] - arr[i])

    return max_sum_bitonic

# Test cases




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)