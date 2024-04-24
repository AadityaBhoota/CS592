def find_min_diff(arr, n): 
    arr.sort() 
    min_diff = arr[1] - arr[0] 
    for i in range(2, n): 
        current_diff = arr[i] - arr[i - 1] 
        if current_diff < min_diff: 
            min_diff = current_diff 
    return min_diff

# Test cases



def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)