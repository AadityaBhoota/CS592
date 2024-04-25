def two_unique_nums(nums):
    """
    Write a python function to remove duplicate numbers from a given list of numbers.

    Examples:
    two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
    """
    return list(set(nums))

def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

check(two_unique_nums)