def common_in_nested_lists(nestedlist):
    common_elements = []

    if not nestedlist:
        return common_elements

    first_list = nestedlist[0]
    
    common_elements.extend(first_list)
    
    for sub_list in nestedlist[1:]:
        common_elements = [element for element in common_elements if element in sub_list]

    return common_elements

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)