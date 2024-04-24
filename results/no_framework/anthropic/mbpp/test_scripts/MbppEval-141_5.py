def pancake_sort(nums):
    """
    Sorts the given list of numbers in ascending order using the Pancake Sort algorithm.

    Args:
        nums (List[int]): The list of numbers to be sorted.

    Returns:
        List[int]: The sorted list of numbers.
    """
    n = len(nums)

    for i in range(n, 0, -1):
        # Find the index of the maximum element in the unsorted part of the list
        max_index = 0
        for j in range(1, i):
            if nums[j] > nums[max_index]:
                max_index = j

        # Flip the list to bring the maximum element to the beginning
        nums[:max_index + 1] = reversed(nums[:max_index + 1])

        # Flip the list to put the maximum element in its correct position
        nums[:i] = reversed(nums[:i])

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)