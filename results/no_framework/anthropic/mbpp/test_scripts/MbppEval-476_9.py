def big_sum(nums):
    """
    Write a python function to find the sum of the largest and smallest value in a given array.

    Examples:
    big_sum([1,2,3]) == 4
    big_sum([-1,2,3,4]) == 3
    big_sum([2,3,6]) == 8
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