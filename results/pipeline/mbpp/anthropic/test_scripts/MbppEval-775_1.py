def odd_position(nums):
    is_odd_position = True
    for i in range(len(nums)):
        if i % 2 == 1 and nums[i] % 2 == 0:
            is_odd_position = False
            break
    return is_odd_position

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False

check(odd_position)