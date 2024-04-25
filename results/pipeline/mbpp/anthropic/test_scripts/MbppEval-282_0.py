def sub_list(nums1, nums2):
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise TypeError("Both inputs must be lists")
    
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