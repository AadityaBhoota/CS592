def common_in_nested_lists(nestedlist):
    common_elements_set = set(nestedlist[0])
    
    # Iterate over the remaining lists in the nested list
    for lst in nestedlist[1:]:
        current_set = set(lst)
        
        # Intersect the current_set with the common_elements_set
        common_elements_set = common_elements_set.intersection(current_set)
    
    # After iterating through all lists
    common_elements_list = list(common_elements_set)
    
    return common_elements_list

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)