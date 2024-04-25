def even_position(nums):
    result = True
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            result = False
            break
    return result

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)