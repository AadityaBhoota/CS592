def two_unique_nums(nums):
    """
    Write a python function to remove duplicate numbers from a given number of lists.

    Examples:
    two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
    """
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]

check(two_unique_nums)