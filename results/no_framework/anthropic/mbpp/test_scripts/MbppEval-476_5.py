def big_sum(nums):
    """
    Find the sum of the largest and smallest value in a given array.

    Args:
        nums (list): A list of numbers.

    Returns:
        int: The sum of the largest and smallest value in the list.
    """
    if not nums:
        return 0

    smallest = min(nums)
    largest = max(nums)
    return smallest + largest

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8

check(big_sum)