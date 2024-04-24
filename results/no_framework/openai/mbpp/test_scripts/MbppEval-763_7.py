def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff

# Test cases



def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)