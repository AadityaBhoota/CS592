def pancake_sort(nums):
    def flip(sub_list, k):
        i = 0
        while i < k // 2:
            sub_list[i], sub_list[k - i - 1] = sub_list[k - i - 1], sub_list[i]
            i += 1
    
    def find_max_index(lst, end):
        max_index = 0
        for i in range(end):
            if lst[i] > lst[max_index]:
                max_index = i
        return max_index
    
    n = len(nums)
    for i in range(n, 1, -1):
        max_index = find_max_index(nums, i)
        if max_index != i - 1:
            flip(nums, max_index + 1)
            flip(nums, i)
    
    return nums

# Test cases




def check(candidate):
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

check(pancake_sort)