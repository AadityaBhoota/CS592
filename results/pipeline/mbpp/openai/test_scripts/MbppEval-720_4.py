def add_dict_to_tuple(test_tup, test_dict):
    new_list = list(test_tup)
    new_list.append(test_dict)
    new_tuple = tuple(new_list)
    return new_tuple

def check(candidate):
    assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
    assert add_dict_to_tuple((1, 2, 3), {"UTS" : 2, "is" : 3, "Worst" : 4} ) == (1, 2, 3, {'UTS': 2, 'is': 3, 'Worst': 4})
    assert add_dict_to_tuple((8, 9, 10), {"POS" : 3, "is" : 4, "Okay" : 5} ) == (8, 9, 10, {'POS': 3, 'is': 4, 'Okay': 5})

check(add_dict_to_tuple)