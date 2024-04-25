def comb_sort(nums):
    gap = len(nums)
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True

    return nums

def check(candidate):
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]

check(comb_sort)