def intersection_array(array_nums1, array_nums2):
    # Convert the input arrays to sets for faster intersection operation
    set1 = set(array_nums1)
    set2 = set(array_nums2)
    
    # Find the intersection of the two sets
    intersection_set = set1.intersection(set2)
    
    # Convert the intersection set back to a list
    intersection_list = list(intersection_set)
    
    return intersection_list

# Test cases




def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

check(intersection_array)