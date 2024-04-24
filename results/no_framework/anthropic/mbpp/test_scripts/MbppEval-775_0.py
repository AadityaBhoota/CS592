def odd_position(nums):
    '''
    Write a python function to check whether every odd index contains odd numbers of a given list.

    Examples:
    odd_position([2,1,4,3,6,7,6,3]) == True
    odd_position([4,1,2]) == True
    odd_position([1,2,3]) == False
    '''
    for i in range(1, len(nums), 2):
        if nums[i] % 2 == 0:
            return False
    return True

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False

check(odd_position)