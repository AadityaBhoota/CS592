def intersection_array(array_nums1, array_nums2):
    num_dict = {}
    for num in array_nums1:
        num_dict[num] = True
    intersection = []
    for num in array_nums2:
        if num in num_dict:
            intersection.append(num)
    return intersection

def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

check(intersection_array)