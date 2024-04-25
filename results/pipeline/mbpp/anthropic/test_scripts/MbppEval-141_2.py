def pancake_sort(nums):
    n = len(nums)
    
    for i in range(n, 0, -1):
        # Find the index of the maximum element in the unsorted part
        max_idx = 0
        for j in range(1, i):
            if nums[j] > nums[max_idx]:
                max_idx = j
        
        # Flip the sublist to bring the maximum element to the beginning
        nums[:max_idx + 1] = reversed(nums[:max_idx + 1])
        
        # Flip the entire unsorted part to bring the maximum element to its correct position
        nums[:i] = reversed(nums[:i])
    
    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)