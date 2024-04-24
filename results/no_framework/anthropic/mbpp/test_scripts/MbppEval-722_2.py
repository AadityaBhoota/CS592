def filter_data(students, min_height, min_weight):
    """
    Filters the students dictionary to include only those with height and weight above the minimum.

    Args:
        students (dict): A dictionary with student names as keys and tuples of (height, weight) as values.
        min_height (float): The minimum height requirement.
        min_weight (float): The minimum weight requirement.

    Returns:
        dict: A new dictionary containing only the students who meet the height and weight requirements.
    """
    return {name: (height, weight) for name, (height, weight) in students.items() if height >= min_height and weight >= min_weight}

def check(candidate):
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.9,67)=={'Cierra Vega': (6.2, 70),'Kierra Gentry': (6.0, 68)}
    assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.7,64)=={'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}

check(filter_data)