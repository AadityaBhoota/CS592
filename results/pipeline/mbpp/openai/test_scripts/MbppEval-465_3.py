def drop_empty(dict1):
    non_empty_dict = {}

    for key, value in dict1.items():
        if value is not None:
            non_empty_dict[key] = value

    return non_empty_dict

def check(candidate):
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}

check(drop_empty)