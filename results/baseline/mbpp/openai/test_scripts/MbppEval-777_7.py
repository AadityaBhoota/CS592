def find_sum(arr):
    unique_elements = set(arr)
    result = sum(element for element in unique_elements if arr.count(element) == 1)
    return result

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)