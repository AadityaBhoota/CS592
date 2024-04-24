def even_position(nums):
    """
    Write a python function to check whether every even index contains even numbers of a given list.

    Examples:
    even_position([3,2,1]) == False
    even_position([1,2,3]) == False
    even_position([2,1,4]) == True
    """
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            return False
    return True

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)