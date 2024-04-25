def even_position(nums):
    for index in range(0, len(nums), 2):
        num = nums[index]
        if index % 2 == 0:
            if num % 2 != 0:
                return False
    return True

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)