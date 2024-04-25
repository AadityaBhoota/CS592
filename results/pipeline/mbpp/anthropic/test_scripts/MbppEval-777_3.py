def find_sum(arr):
    """
    Write a python function to find the sum of non-repeated elements in a given list.

    Examples:
    find_sum([1,2,3,1,1,4,5,6]) == 21
    find_sum([1,10,9,4,2,10,10,45,4]) == 71
    find_sum([12,10,9,45,2,10,10,45,10]) == 78
    """
    unique_elements = set(arr)
    return sum(unique_elements)

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)