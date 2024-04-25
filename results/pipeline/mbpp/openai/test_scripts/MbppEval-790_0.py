def even_position(nums):
    result = True
    for index, value in enumerate(nums):
        if index % 2 == 0 and value % 2 != 0:
            result = False
            break
    return result

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)