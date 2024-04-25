def pluck(arr):
    """
    Pluck the node with the smallest even value from the given array.

    Args:
        arr (list): An array representing a branch of a tree with non-negative integer nodes.

    Returns:
        list: A list containing the smallest even value and its index, if found. Otherwise, an empty list.
    """
    if not arr:
        return []

    even_values = [value for value in arr if value % 2 == 0]
    if not even_values:
        return []

    smallest_even = min(even_values)
    smallest_index = next(i for i, x in enumerate(arr) if x == smallest_even)

    return [smallest_even, smallest_index]

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([4,2,3]) == [2, 1], "Error"
    assert candidate([1,2,3]) == [2, 1], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
    assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error"
    assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
    assert candidate([7, 9, 7, 1]) == [], "Error"


check(pluck)