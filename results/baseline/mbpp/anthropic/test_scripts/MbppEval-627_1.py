def find_First_Missing(array, start=0, end=None):
    """
    Finds the smallest missing number from a sorted list of natural numbers.

    Args:
        array (list): A sorted list of natural numbers.
        start (int, optional): The starting index of the array. Defaults to 0.
        end (int, optional): The ending index of the array. Defaults to None, which means the entire array.

    Returns:
        int: The smallest missing number from the array.
    """
    if end is None:
        end = len(array) - 1

    # Base case: If the array is empty, the smallest missing number is 0
    if start > end:
        return 0

    # Base case: If the first element is not 0, the smallest missing number is 0
    if array[start] != 0:
        return 0

    # Base case: If the last element is the length of the array, the smallest missing number is the length of the array + 1
    if array[end] == end - start:
        return end - start + 1

    # Recursive case: Find the middle element and check if the difference between the middle element and its index is 1
    mid = (start + end) // 2
    if array[mid] == mid - start:
        return find_First_Missing(array, mid + 1, end)
    else:
        return find_First_Missing(array, start, mid)

def check(candidate):
    assert find_First_Missing([0,1,2,3]) == 4
    assert find_First_Missing([0,1,2,6,9]) == 3
    assert find_First_Missing([2,3,5,8,9]) == 0

check(find_First_Missing)