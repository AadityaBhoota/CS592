def div_list(nums1, nums2):
    """
    Write a function to divide two lists element-wise.

    Examples:
    div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
    div_list([3, 2], [1, 4]) == [3.0, 0.5]
    div_list([90, 120], [50, 70]) == [1.8, 1.7142857142857142]
    """
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must have the same length.")

    return [a / b for a, b in zip(nums1, nums2)]

def check(candidate):
    assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
    assert div_list([3,2],[1,4])==[3.0, 0.5]
    assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]

check(div_list)