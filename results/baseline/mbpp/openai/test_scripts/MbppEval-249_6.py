def intersection_array(array_nums1, array_nums2):
    set1 = set(array_nums1)
    set2 = set(array_nums2)
    intersection = list(set1.intersection(set2))
    return intersection

# Test cases




def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

check(intersection_array)