def even_position(nums):
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 != 0:
            return False
    return True

# Test cases




def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)