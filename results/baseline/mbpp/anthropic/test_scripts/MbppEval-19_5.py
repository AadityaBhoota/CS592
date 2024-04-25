def test_duplicate(arraynums):
    """
    Write a function to find whether a given array of integers contains any duplicate element.

    Examples:
    test_duplicate(([1,2,3,4,5])) == False
    test_duplicate(([1,2,3,4, 4])) == True
    test_duplicate([1,1,2,2,3,3,4,4,5]) == True
    """
    # Create a set to store unique elements
    unique_elements = set()

    # Iterate through the array
    for num in arraynums:
        # If the element is already in the set, return True (duplicate found)
        if num in unique_elements:
            return True
        # Otherwise, add the element to the set
        unique_elements.add(num)

    # If we made it through the entire array without finding a duplicate, return False
    return False

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

check(test_duplicate)