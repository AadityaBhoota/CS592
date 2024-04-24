def max_sum(arr):
    n = len(arr)
    
    # Create two arrays to store the increasing and decreasing subsequence sums
    increasing = [0] * n
    decreasing = [0] * n
    
    # Compute the increasing subsequence sums
    for i in range(n):
        max_sum = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_sum = max(max_sum, increasing[j])
        increasing[i] = max_sum + arr[i]
    
    # Compute the decreasing subsequence sums
    for i in range(n-1, -1, -1):
        max_sum = 0
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                max_sum = max(max_sum, decreasing[j])
        decreasing[i] = max_sum + arr[i]
    
    # Find the maximum sum of the bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, increasing[i] + decreasing[i] - arr[i])
    
    return max_bitonic_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)