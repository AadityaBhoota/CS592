def count_rotation(arr):   
    '''
    Write a python function to count the number of rotations required to generate a sorted array. 
    Examples:
    count_Rotation([3,2,1],3) == 1
    count_Rotation([4,5,1,2,3],5) == 2
    count_Rotation([7,8,9,1,2,3],6) == 3
    '''
    
    # Implementing Step 0
    def count_rotation(arr):
        return len(arr)

    length = count_rotation(arr)
    
    # Implementing Step 2
    copied_arr = arr.copy()
    
    # Implementing Step 3
    copied_arr.sort()
    
    # Implementing Step 4
    for i in range(length):
        if arr[i] == copied_arr[0]:
            return i

def check(candidate):
    assert count_rotation([3,2,1]) == 1
    assert count_rotation([4,5,1,2,3]) == 2
    assert count_rotation([7,8,9,1,2,3]) == 3
    assert count_rotation([1,2,3]) == 0
    assert count_rotation([1,3,2]) == 2

check(count_rotation)