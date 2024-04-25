def odd_position(nums):
    for index, num in enumerate(nums):
        if index % 2 == 1:
            if num % 2 == 0:
                return False
    return True

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False

check(odd_position)