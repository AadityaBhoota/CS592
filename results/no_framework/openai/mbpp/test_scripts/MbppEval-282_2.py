def sub_list(nums1, nums2):
    return [n1 - n2 for n1, n2 in zip(nums1, nums2)]

# Test cases




def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]

check(sub_list)