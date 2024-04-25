def dict_filter(d, n):
    """
    Filters a dictionary to include only entries with values greater than or equal to n.
    
    Args:
        d (dict): The dictionary to be filtered.
        n (int): The minimum value for an entry to be included.
    
    Returns:
        dict: The filtered dictionary.
    """
    return {k: v for k, v in d.items() if v >= n}

def check(candidate):
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}

check(dict_filter)