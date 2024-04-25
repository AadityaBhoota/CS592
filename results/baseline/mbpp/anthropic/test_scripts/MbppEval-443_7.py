def largest_neg(list1):
    """
    Write a python function to find the largest negative number from the given list.

    Examples:
    largest_neg([1,2,3,-4,-6]) == -4
    largest_neg([1,2,3,-8,-9]) == -8
    largest_neg([1,2,3,4,-1]) == -1
    """
    # Create a list of only the negative numbers
    neg_nums = [num for num in list1 if num < 0]

    # If the list of negative numbers is empty, return None
    if not neg_nums:
        return None

    # Find the largest negative number
    largest = max(neg_nums)
    return largest

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)