def count_rotation(arr):
    min_element = float('inf')
    rotation_count = 0

    for i, num in enumerate(arr):
        if num < min_element:
            min_element = num
            rotation_count = i

    return rotation_count

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)