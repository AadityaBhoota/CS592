def find_First_Missing(array, start=0, end=None):
    """
    Write a python function to find the smallest missing number from a sorted list of natural numbers.

    Examples:
    find_First_Missing([0, 1, 2, 3], 0, 3) == 4
    find_First_Missing([0, 1, 2, 6, 9], 0, 4) == 3
    find_First_Missing([2, 3, 5, 8, 9], 0, 4) == 0
    """
    if end is None:
        end = len(array) - 1

    # Base case: If the array is empty, the first missing number is 0
    if end < start:
        return 0

    # Check if the first element is not 0
    if array[start] != 0:
        return 0

    # Recursive case: Find the first missing number
    for i in range(start, end + 1):
        if i != array[i]:
            return i

    # If all elements in the array are consecutive, the first missing number is the next number
    return array[end] + 1

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)