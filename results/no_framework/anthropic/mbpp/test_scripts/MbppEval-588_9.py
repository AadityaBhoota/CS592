def big_diff(nums):
    """
    Write a python function to find the difference between largest and smallest value in a given list.

    Examples:
    big_diff([1,2,3,4]) == 3
    big_diff([4,5,12]) == 8
    big_diff([9,2,3]) == 7
    """
    if not nums:
        return 0

    # Find the largest and smallest values in the list
    max_value = max(nums)
    min_value = min(nums)

    # Calculate the difference between the largest and smallest values
    return max_value - min_value

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7

check(big_diff)