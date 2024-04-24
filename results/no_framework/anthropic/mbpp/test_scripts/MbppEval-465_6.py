def drop_empty(dict1):
    """
    Write a function to drop empty items from a given dictionary.

    Examples:
    drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}) == {'c1': 'Red', 'c2': 'Green'}
    drop_empty({'c1': 'Red', 'c2': None, 'c3':None}) == {'c1': 'Red'}
    drop_empty({'c1': None, 'c2': 'Green', 'c3':None}) == {'c2': 'Green'}
    """
    return {k: v for k, v in dict1.items() if v}

def check(candidate):
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}

check(drop_empty)