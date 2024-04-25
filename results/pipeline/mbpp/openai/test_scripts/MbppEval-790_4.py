def even_position(nums):
    even_position_all_even = True
    
    for index, num in enumerate(nums):
        if index % 2 == 0:
            if num % 2 != 0:
                even_position_all_even = False
                break
                
    return even_position_all_even

# Test the function




def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True

check(even_position)