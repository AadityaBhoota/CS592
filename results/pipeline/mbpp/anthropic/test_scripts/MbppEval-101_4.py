def kth_element(arr, k):
    if not arr:
        raise ValueError("Input array cannot be empty.")
    if k < 1 or k > len(arr):
        raise ValueError("k must be within the range [1, len(arr)].")
    
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)