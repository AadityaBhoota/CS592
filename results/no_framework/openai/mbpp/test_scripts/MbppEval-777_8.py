def find_sum(arr):
    non_repeated_elements = [x for x in arr if arr.count(x) == 1]
    return sum(non_repeated_elements)

# Test cases




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)