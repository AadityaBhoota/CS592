def dict_filter(dict_data, n):
    """
    Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.

    Examples:
    dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170) == {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180) == {'Alden Cantrell': 180, 'Pierre Cox': 190}
    dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190) == {'Pierre Cox': 190}
    """
    return {k: v for k, v in dict_data.items() if v >= n}

def check(candidate):
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}

check(dict_filter)