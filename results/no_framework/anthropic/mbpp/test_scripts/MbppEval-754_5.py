def extract_index_list(l1, l2, l3):
    """
    Find common elements from three lists that appear in all three lists under the same index.
    
    Args:
    l1 (list): The first list.
    l2 (list): The second list.
    l3 (list): The third list.
    
    Returns:
    list: A list of common elements that appear in all three lists under the same index.
    """
    # Check if the lengths of the three lists are equal
    if len(l1) != len(l2) or len(l2) != len(l3):
        return []
    
    # Iterate through the lists and find common elements
    common_elements = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    
    return common_elements

def check(candidate):
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 6, 5],[0, 1, 2, 3, 4, 6, 7])==[1, 6]
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]
    assert extract_index_list([1, 2, 3, 4, 6, 6, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[]

check(extract_index_list)