def extract_index_list(l1, l2, l3):
    common_elements = []
    min_len = min(len(l1), len(l2), len(l3))

    for i in range(min_len):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])

    return common_elements

# Testing the function with examples




def check(candidate):
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 6, 5],[0, 1, 2, 3, 4, 6, 7])==[1, 6]
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]
    assert extract_index_list([1, 2, 3, 4, 6, 6, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[]

check(extract_index_list)