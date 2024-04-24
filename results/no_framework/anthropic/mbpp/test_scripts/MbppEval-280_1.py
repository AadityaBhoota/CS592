def sequential_search(dlist, item):
    """
    Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).

    Examples:
    sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)
    """
    for i, elem in enumerate(dlist):
        if elem == item:
            return (True, i)
    return (False, -1)

def check(candidate):
    assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)

check(sequential_search)