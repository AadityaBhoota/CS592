def is_sorted(lst):
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    """
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True

    # Create a set to store the unique elements
    unique_elements = set()

    # Iterate through the list and check if the elements are in ascending order
    for i in range(len(lst) - 1):
        # If the current element is greater than the next element, return False
        if lst[i] >= lst[i + 1]:
            return False

        # Add the current element to the set
        unique_elements.add(lst[i])

    # Add the last element to the set
    unique_elements.add(lst[-1])

    # If the length of the set is not equal to the length of the list, return False
    return len(unique_elements) == len(lst)

def check(candidate):

    # Check some simple cases
    assert candidate([5]) == True
    assert candidate([1, 2, 3, 4, 5]) == True
    assert candidate([1, 3, 2, 4, 5]) == False
    assert candidate([1, 2, 3, 4, 5, 6]) == True
    assert candidate([1, 2, 3, 4, 5, 6, 7]) == True
    assert candidate([1, 3, 2, 4, 5, 6, 7]) == False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == True, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate([1]) == True, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate([3, 2, 1]) == False, "This prints if this assert fails 4 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 2, 2, 3, 4]) == False, "This prints if this assert fails 5 (good for debugging!)"
    assert candidate([1, 2, 3, 3, 3, 4]) == False, "This prints if this assert fails 6 (good for debugging!)"
    assert candidate([1, 2, 2, 3, 3, 4]) == True, "This prints if this assert fails 7 (good for debugging!)"
    assert candidate([1, 2, 3, 4]) == True, "This prints if this assert fails 8 (good for debugging!)"


check(is_sorted)