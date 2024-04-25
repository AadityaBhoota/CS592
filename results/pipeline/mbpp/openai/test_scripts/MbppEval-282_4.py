def sub_list(nums1, nums2):
    return [nums1[i] - nums2[i] for i in range(min(len(nums1), len(nums2))]

def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]

check(sub_list)