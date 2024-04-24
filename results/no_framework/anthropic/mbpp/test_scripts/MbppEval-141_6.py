def pancake_sort(nums):
    """
    Sorts the given list of elements using the pancake sort algorithm.

    Args:
        nums (list): The list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    n = len(nums)
    for i in range(n, 0, -1):
        # Find the maximum element in the unsorted part of the list
        max_idx = nums.index(i)

        # Reverse the elements from the beginning to the maximum element
        nums[:max_idx + 1] = reversed(nums[:max_idx + 1])

        # Reverse the entire list to put the maximum element in its correct position
        nums[:i] = reversed(nums[:i])

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)