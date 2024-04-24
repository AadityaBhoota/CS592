def drop_empty(dict1):
    return {k: v for k, v in dict1.items() if v is not None}

# Test cases




def check(candidate):
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}

check(drop_empty)