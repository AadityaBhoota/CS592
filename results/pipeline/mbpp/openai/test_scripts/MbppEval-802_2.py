def count_rotation(arr):
    if not arr:
        return "Invalid input. Please provide a non-empty list."
    
    min_index = arr.index(min(arr))
    num_rotations = min_index
    return num_rotations

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)