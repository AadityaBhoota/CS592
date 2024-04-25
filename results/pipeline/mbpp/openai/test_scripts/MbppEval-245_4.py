def max_sum(arr): 
    '''
    Finds the maximum sum of a bitonic subsequence for the given array.
    
    Args:
    arr (list): Input array
    
    Returns:
    int: Maximum sum of a bitonic subsequence
    '''
    n = len(arr)
    increasing = [0] * n
    decreasing = [0] * n
    bitonic = [0] * n

    for i in range(n):
        increasing[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j] + arr[i])

    for i in range(n - 1, -1, -1):
        decreasing[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + arr[i])

    for i in range(n):
        bitonic[i] = increasing[i] + decreasing[i] - arr[i]

    max_sum = max(bitonic)

    return max_sum

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)