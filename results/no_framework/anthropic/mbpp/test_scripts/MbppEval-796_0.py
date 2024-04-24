def return_sum(dictionary):
    """
    Finds the sum of all values in the given dictionary.

    Args:
        dictionary (dict): The dictionary to find the sum of all values.

    Returns:
        int: The sum of all values in the dictionary.
    """
    return sum(dictionary.values())

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124

check(return_sum)