def move_zero(num_list):
    """
    Write a python function to move all zeroes to the end of the given list.

    Examples:
    move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    move_zero([0,1,0,1,1]) == [1,1,1,0,0]
    """
    non_zero = [i for i in num_list if i != 0]
    zero = [i for i in num_list if i == 0]
    return non_zero + zero

def check(candidate):
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]

check(move_zero)