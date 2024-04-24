def find_First_Missing(array, start=0, end=None):
    """
    Write a python function to find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_First_Missing([0,1,2,3],0,3) == 4
    find_First_Missing([0,1,2,6,9],0,4) == 3
    find_First_Missing([2,3,5,8,9],0,4) == 0
    """
    if end is None:
        end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid + start:
            start = mid + 1
        else:
            end = mid - 1

    return start

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)