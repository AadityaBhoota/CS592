def dict_filter(dictionary, n):
    """
    Filters a dictionary to include only entries with values greater than or equal to n.
    
    Args:
    dictionary (dict): The dictionary to filter.
    n (int): The minimum value to include in the filtered dictionary.
    
    Returns:
    dict: A new dictionary containing only the entries from the original dictionary with values greater than or equal to n.
    """
    return {key: value for key, value in dictionary.items() if value >= n}

def check(candidate):
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}

check(dict_filter)