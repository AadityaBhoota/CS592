def kth_element(arr, size, k):
    if k > size or k < 1:
        return None
    return arr[k-1]

# Test cases




def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)