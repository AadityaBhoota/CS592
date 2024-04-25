def kth_element(arr, k):
    if k <= 0 or k > len(arr):
        return "Invalid value of k"
    
    return arr[k-1]

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)