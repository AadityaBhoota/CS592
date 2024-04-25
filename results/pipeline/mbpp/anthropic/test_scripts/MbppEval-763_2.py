def find_min_diff(arr, n):
    if n < 2:
        return 0

    # Initialize min_diff to a very large value
    min_diff = float('inf')

    # Sort the input array
    arr.sort()

    # Iterate through the sorted array, calculating the difference between adjacent elements
    for i in range(1, n):
        diff = abs(arr[i] - arr[i - 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)