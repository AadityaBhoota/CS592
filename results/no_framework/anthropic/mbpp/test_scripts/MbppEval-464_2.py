def check_value(d, n):
    """
    Write a function to check if all values in a dictionary are the same as the given value.

    Args:
        d (dict): The dictionary to check.
        n (int): The value to check against.

    Returns:
        bool: True if all values in the dictionary are equal to n, False otherwise.
    """
    return all(value == n for value in d.values())

def check(candidate):
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False

check(check_value)