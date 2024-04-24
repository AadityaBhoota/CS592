def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Find the maximum increasing sum ending at each index
    increasing = [0] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j])
        increasing[i] += arr[i]

    # Find the maximum decreasing sum starting at each index
    decreasing = [0] * n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j])
        decreasing[i] += arr[i]

    # Find the maximum bitonic sum
    bitonic_sum = 0
    for i in range(n):
        bitonic_sum = max(bitonic_sum, increasing[i] + decreasing[i] - arr[i])

    return bitonic_sum

# Examples




def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)