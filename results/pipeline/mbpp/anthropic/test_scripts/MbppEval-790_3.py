def even_position(nums):
    is_even_position = True
    for i, num in enumerate(nums):
        if i % 2 == 0 and num % 2 != 0:
            is_even_position = False
            break
    return is_even_position

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)