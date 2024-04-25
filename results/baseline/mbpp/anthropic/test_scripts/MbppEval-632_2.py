def move_zero(num_list):
    """
    Write a python function to move all zeroes to the end of the given list.

    Examples:
    move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    move_zero([0,1,0,1,1]) == [1,1,1,0,0]
    """
    non_zeros = [num for num in num_list if num != 0]
    zeros = [num for num in num_list if num == 0]
    return non_zeros + zeros

def check(candidate):
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]

check(move_zero)