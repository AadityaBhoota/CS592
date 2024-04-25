def list_to_float(test_list):
    modified_list = []
    for sublist in test_list:
        modified_sublist = []
        for element in sublist:
            try:
                modified_sublist.append(float(element))
            except ValueError:
                modified_sublist.append(element)
        modified_list.append(tuple(modified_sublist))  # Convert to tuple before appending
    return modified_list

def check(candidate):
    assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
    assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == [(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]
    assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == [(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]

check(list_to_float)