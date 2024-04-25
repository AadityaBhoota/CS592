def move_zero(num_list):
    zeros = []
    non_zeros = []
    
    for num in num_list:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    
    return non_zeros + zeros

def check(candidate):
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]

check(move_zero)