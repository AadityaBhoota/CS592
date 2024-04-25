def count_rotation(arr):   
    # Step 0: Check if the array is empty
    if not arr:
        return 0
    
    # Step 1: Find the index of the minimum element in the array
    min_index = arr.index(min(arr))
    
    # Step 2: Return the number of rotations required
    return len(arr) - min_index

# Test the function with given examples




def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)