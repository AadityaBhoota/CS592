def comb_sort(nums):
    gap = len(nums)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(nums):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted = False
            i += 1

    return nums

def check(candidate):
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]

check(comb_sort)