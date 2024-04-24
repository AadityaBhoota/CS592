def largest_neg(list1):
    """
    Write a python function to find the largest negative number from the given list.

    Examples:
    largest_neg([1,2,3,-4,-6]) == -4
    largest_neg([1,2,3,-8,-9]) == -8
    largest_neg([1,2,3,4,-1]) == -1
    """
    negative_numbers = [num for num in list1 if num < 0]
    if negative_numbers:
        return max(negative_numbers)
    else:
        return None

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1

check(largest_neg)