def dict_filter(dictionary, n):
    """
    Filters a dictionary to only include entries with values greater than or equal to n.

    Args:
        dictionary (dict): The input dictionary to be filtered.
        n (int): The minimum value for an entry to be included in the filtered dictionary.

    Returns:
        dict: The filtered dictionary.
    """
    return {key: value for key, value in dictionary.items() if value >= n}

def check(candidate):
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}

check(dict_filter)