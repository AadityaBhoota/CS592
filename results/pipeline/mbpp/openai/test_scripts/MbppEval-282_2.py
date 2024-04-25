def sub_list(nums1, nums2):
    if len(nums1) != len(nums2):
        return "Error: Lists must be of equal length"
    
    result = []
    for n1, n2 in zip(nums1, nums2):
        result.append(n1 - n2)
    return result

def check(candidate):
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert sub_list([1,2],[3,4])==[-2,-2]
    assert sub_list([90,120],[50,70])==[40,50]

check(sub_list)