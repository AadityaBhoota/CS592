def even_position(nums):
    all_even_index_even = True

    for i in range(len(nums)):
        if i % 2 == 0:
            if nums[i] % 2 != 0:
                all_even_index_even = False
                break

    return all_even_index_even

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)