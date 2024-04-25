def first_odd(nums):
    """
    Write a python function to find the first odd number in a given list of numbers.

    Examples:
    first_odd([1,3,5]) == 1
    first_odd([2,4,1,3]) == 1
    first_odd ([8,9,1]) == 9
    """
    for num in nums:
        if num % 2 == 1:
            return num
    return None

def check(candidate):
    assert first_odd([1,3,5]) == 1
    assert first_odd([2,4,1,3]) == 1
    assert first_odd ([8,9,1]) == 9

check(first_odd)