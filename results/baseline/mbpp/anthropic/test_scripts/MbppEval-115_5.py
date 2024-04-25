def empty_dit(lst):
    """
    Checks whether all dictionaries in a list are empty or not.

    Args:
        lst (list): A list of dictionaries.

    Returns:
        bool: True if all dictionaries in the list are empty, False otherwise.
    """
    if isinstance(lst, dict):
        return len(lst) == 0
    elif isinstance(lst, list):
        return all(len(d) == 0 for d in lst)
    else:
        return False

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)