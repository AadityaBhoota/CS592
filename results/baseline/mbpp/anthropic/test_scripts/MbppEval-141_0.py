def pancake_sort(nums):
    """
    Sort a list of elements using the pancake sort algorithm.

    Args:
        nums (list): A list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    n = len(nums)

    # Perform the pancake sort
    for i in range(n, 0, -1):
        # Find the maximum element in the unsorted part of the list
        max_index = max(range(i), key=lambda x: nums[x])

        # Flip the list to bring the maximum element to the front
        nums = nums[:max_index + 1][::-1] + nums[max_index + 1:]

        # Flip the list to place the maximum element at the end
        nums = nums[:i][::-1] + nums[i:]

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)