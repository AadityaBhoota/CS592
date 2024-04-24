def find_First_Missing(array, start=0, end=None):
    """
    Write a python function to find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_First_Missing([0,1,2,3],0,3) == 4
    find_First_Missing([0,1,2,6,9],0,4) == 3
    find_First_Missing([2,3,5,8,9],0,4) == 0
    """
    if not array:
        return 0

    if end is None:
        end = len(array) - 1

    if array[start] != 0:
        return 0

    if array[end] == end - start:
        return array[end] + 1

    left = start
    right = end

    while left <= right:
        mid = (left + right) // 2
        expected = mid - start
        if array[mid] == expected:
            left = mid + 1
        else:
            right = mid - 1

    return left + start

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)