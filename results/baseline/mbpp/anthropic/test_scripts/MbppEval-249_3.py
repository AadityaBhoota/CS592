def intersection_array(array_nums1, array_nums2):
    """
    Write a function to find the intersection of two arrays.

    Examples:
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]) == [1, 2, 8, 9]
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9]) == [3,5,7,9]
    intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40]) == [10]
    """
    # Convert the second array to a set for faster lookup
    set_nums2 = set(array_nums2)
    
    # Filter the first array to only include elements that are also in the second array
    intersection = [num for num in array_nums1 if num in set_nums2]
    
    return intersection

def check(candidate):
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

check(intersection_array)