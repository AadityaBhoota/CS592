def largest_neg(list1):
    """
    Write a python function to find the largest negative number from the given list.

    Examples:
    largest_neg([1,2,3,-4,-6]) == -4
    largest_neg([1,2,3,-8,-9]) == -8
    largest_neg([1,2,3,4,-1]) == -1
    """
    # Initialize the largest negative number to a very small value
    largest_neg_num = float('-inf')

    # Iterate through the list and update the largest negative number
    for num in list1:
        if num < 0 and num > largest_neg_num:
            largest_neg_num = num

    # If no negative numbers are found, return None
    if largest_neg_num == float('-inf'):
        return None

    return largest_neg_num

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)