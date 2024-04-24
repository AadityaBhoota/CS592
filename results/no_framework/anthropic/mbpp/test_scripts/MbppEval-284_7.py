def check_element(lst, element):
    """
    Checks whether all items in the list are equal to the given element.

    Args:
        lst (list): The list to be checked.
        element: The element to compare against.

    Returns:
        bool: True if all items in the list are equal to the given element, False otherwise.
    """
    return all(x == element for x in lst)

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)