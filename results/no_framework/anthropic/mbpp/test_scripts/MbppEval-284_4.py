def check_element(lst, element):
    """
    Write a function that takes in a list and element and checks whether all items in the list are equal to the given element.

    Examples:
    check_element(["green", "orange", "black", "white"], 'blue') == False
    check_element([1, 2, 3, 4], 7) == False
    check_element(["green", "green", "green", "green"], 'green') == True
    """
    return all(item == element for item in lst)

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)