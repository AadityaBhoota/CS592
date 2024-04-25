def sub_list(nums1, nums2):
    """
    Write a function to subtract two lists element-wise.

    Examples:
    sub_list([1, 2, 3],[4,5,6]) == [-3,-3,-3]
    sub_list([1,2],[3,4]) == [-2,-2]
    sub_list([90,120],[50,70]) == [40,50]
    """
    if len(nums1) != len(nums2):
        raise ValueError("Lists must have the same length")

    result = []
    for i in range(len(nums1)):
        result.append(nums1[i] - nums2[i])

    return result

def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]

check(sub_list)