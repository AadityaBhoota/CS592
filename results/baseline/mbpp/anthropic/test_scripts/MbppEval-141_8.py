def pancake_sort(nums):
    """
    Sort a list of elements using the Pancake Sort algorithm.

    Args:
        nums (list): A list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    n = len(nums)

    for i in range(n, 0, -1):
        # Find the maximum element in the current range
        max_idx = 0
        for j in range(1, i):
            if nums[j] > nums[max_idx]:
                max_idx = j

        # Flip the sublist to bring the maximum element to the beginning
        nums = nums[:max_idx+1][::-1] + nums[max_idx+1:]

        # Flip the entire sublist to put the maximum element in its correct position
        nums = nums[:i][::-1] + nums[i:]

    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)