def pos_count(nums):
    """
    Write a Python function to count the number of positive numbers in a list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The count of positive numbers in the list.
    """
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4

check(pos_count)