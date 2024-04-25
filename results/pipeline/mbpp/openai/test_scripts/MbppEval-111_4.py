def common_in_nested_lists(nestedlist):
    common_elements = set(nestedlist[0])  # Step 0
    
    for nested_list in nestedlist:  # Step 1 corrected
        common_elements = common_elements.intersection(set(nested_list))  # Step 2
        
    return list(common_elements)  # Step 3

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)