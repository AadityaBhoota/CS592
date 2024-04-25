def pancake_sort(nums):
    def find_max_index(lst):
        return max(range(len(lst)), key=lst.__getitem__)
    
    def flip(lst, k):
        return lst[:k+1][::-1] + lst[k+1:]
    
    n = len(nums)
    for size in range(n, 1, -1):
        max_index = find_max_index(nums[:size])
        if max_index != size - 1:
            nums = flip(nums, max_index)
            nums = flip(nums, size - 1)
    
    return nums

def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)